import os
import sys
import numpy as np
import tensorflow as tf

from ray import tune
from wandb.keras import WandbCallback
from ray.tune.integration.keras import TuneReportCallback

from efficient_det.losses import smooth_l1, focal_loss
from efficient_det.utils.logs import initialize_logging
from efficient_det.utils.parser import parse_args, get_file_names_for_dataset
from efficient_det.models.efficient_det import efficientdet, my_init
from efficient_det.callbacks.eval import Evaluate
from efficient_det.preprocessing.generator import FruitDatasetGenerator
from efficient_det.configuration.model_params import efficientdet_params as edet
from efficient_det.configuration.model_params import efficientnet_params as enet
from efficient_det.utils.model_service import (activation_from_config,
                                               optimizer_from_config)


def load_data(config):
    """ Loads data from file and processes them to Generators

    Args:
        config: Includes all model and run settings.

    Returns: train_ds: FruitDatasetGenerator, val_ds: FruitDatasetGenerator

    """
    phi = config['phi']
    train_data = get_file_names_for_dataset("trainval",
                                            path=config['dataset_path'])
    val_data = get_file_names_for_dataset("trainval",
                                          path=config['dataset_path'])

    annotations_path = os.path.join(config['dataset_path'], "Annotations/")
    image_path = os.path.join(config['dataset_path'], "JPEGImages/")

    train_ds = FruitDatasetGenerator(train_data, annotations_path, image_path,
                                     batch_size=config['batch_size'],
                                     image_shape=edet[phi][0])
    val_ds = FruitDatasetGenerator(val_data, annotations_path, image_path,
                                   batch_size=config['batch_size'],
                                   image_shape=edet[phi][0])

    return train_ds, val_ds


def model_from_config(config):
    """ Create model.

    Args:
        config: Includes all model and run settings.

    Returns: Compiled model.

    """
    phi = config['phi']
    efficient_net_params = enet[edet[phi][1]][0:3]
    fpn_params = edet[phi][2:4]
    pred_params = edet[phi][3:5]

    optimizer = optimizer_from_config(config)
    activation = activation_from_config(config)

    train_model = efficientdet(input_shape=edet[phi][0],
                               enet_params=efficient_net_params,
                               fpn_params=fpn_params, pred_params=pred_params,
                               activation_func=activation)

    train_model.compile(optimizer=optimizer, loss={"regression": smooth_l1,
                                                   "classification":
                                                       focal_loss})

    return train_model


def distributed_training(config, data_dir=None, checkpoint_dir=None):
    """ Runs a distributed training with ray tune to sweep the hyperpameter
    space. Both data_dir and checkpoint_dir don't need to be set, they serve
    internal ray processes.

    Args:
    config (dict): Includes all model and run settings.
    data_dir (string, optional): Path to enable data parallelization
    checkpoint_dir (string, optional): Checkpoint path for ray tune
        defaults to tune.checkpoint_dir().

    """

    train_ds, val_ds = load_data(config)
    train_model = model_from_config(config)

    # Mapping from ray tune metric name as key to tensorflow metric name
    metric_dict = {'val_loss': 'val_loss',
                   'val_classification_loss': 'val_classification_loss',
                   'val_regression_loss': 'val_regression_loss',
                   'train_loss': 'loss',
                   'train_classification_loss': 'classification_loss',
                   'train_regression_loss': 'regression_loss'}

    if config['evaluation']:
        metric_dict['mAP'] = 'mAP'

    callbacks = create_callbacks(val_ds, config=config)
    callbacks.append(TuneReportCallback(metric_dict))

    with tune.checkpoint_dir(0) as checkpoint_dir:
        model_path = os.path.join(checkpoint_dir, "model_checkpoint")

    # Ray Tune handles the number of iterations
    train_model.fit(train_ds, epochs=config['num_epochs'], verbose=0,
                    validation_data=val_ds, callbacks=callbacks)


def create_callbacks(val_ds, config):
    """

    Args:
        val_ds: Validation dataset generator.
        config:

    Returns:

    """
    callbacks = []

    if config['evaluation']:
        callbacks.append(
            Evaluate(generator=val_ds, use_wandb=config['use_wandb']))

    if config['save_model']:
        try:
            os.mkdir(config['save_dir'])
        except OSError as error:
            print("Save directory already exists.")

        save_path = os.path.join(config['save_dir'],
                                 "test_model_{epoch:02d}.h5")

        if config['evaluation']:
            mode = 'max'
            monitor = 'mAP'
        else:
            mode = 'min'
            monitor = 'val_loss'

        checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
            filepath=save_path, save_weights_only=False,
            save_freq=int(config['save_freq']), mode=mode, monitor=monitor,
            verbose=1)
        callbacks.append(checkpoint_callback)

    if config['use_wandb']:
        initialize_logging(config)
        callbacks.append(WandbCallback())

    return callbacks


def run_training(config):
    """Runs an efficient det model with the defined parameters in the
    config

    Args:
        config (dict): contains all parameter to initialize the training
    """

    train_ds, val_ds = load_data(config)

    tf.compat.v1.enable_eager_execution()
    tf.executing_eagerly()

    tf.random.set_seed(522)
    np.random.seed(522)

    if config['load_model']:
        train_model = tf.keras.models.load_model(config['load_path'],
                                                 custom_objects={
                                                     'focal_loss': focal_loss,
                                                     'smooth_l1': smooth_l1,
                                                     'my_init': my_init})
        print('Model loaded from disk')
    else:
        train_model = model_from_config(config)

    callbacks = create_callbacks(val_ds=val_ds, config=config)

    train_model.fit(train_ds, epochs=config['num_epochs'], verbose=1,
                    validation_data=val_ds, callbacks=callbacks)


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    args = parse_args(args)

    config = {'optimizer': "adam", 'learning_rate': 5e-4,
              'num_epochs': args.epochs, 'activations': "relu",
              'batch_size': args.batch_size, 'dataset_path': args.dataset_path,
              'phi': args.phi, 'evaluation': args.evaluation,
              'use_wandb': args.use_wandb, 'save_model': args.save_model,
              'save_freq': args.save_freq, 'save_dir': args.save_dir,
              'load_model': args.load_model, 'load_path': args.load_path}

    if len(tf.config.experimental.list_physical_devices('GPU')):
        DEVICE = "/gpu:0"
        print("Use GPU")
    else:
        DEVICE = "/cpu:0"
        print("Use CPU")

    with tf.device(DEVICE):
        run_training(config=config)


if __name__ == "__main__":
    os.environ['WANDB_API_KEY'] = ''
    main()
