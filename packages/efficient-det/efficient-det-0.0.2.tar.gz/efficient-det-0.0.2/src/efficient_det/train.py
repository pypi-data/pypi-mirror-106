import os
import sys
import argparse
import warnings
import tensorflow as tf
import numpy as np

from ray import tune
from numpy.random import seed
from configuration.model_params import efficientdet_params as edet
from configuration.model_params import efficientnet_params as enet
from preprocessing.generator import FruitDatasetGenerator
from losses import smooth_l1, focal_loss
from models.efficient_det import efficientdet

from layers.swish import Swish
from ray.tune.integration.keras import TuneReportCallback
from wandb.keras import WandbCallback
from utils.logs import initialize_logging, report_scores


def get_file_names_for_dataset(name="train",
                               path="/Users/zeynep068/efficientdet/voc_data/"):
    path = os.path.join(path, "ImageSets/Main/")
    file_names = []

    for entry in os.listdir(path):
        if entry.endswith(str(name + ".txt")):
            for line in open(os.path.join(path, entry)).readlines():
                if line[-3:-1] == " 1":
                    file_names.append(line[:-3])
    return list(set(file_names))


def load_data(config, path, phi):
    """ Loads data from file and processes them to Generators

    Args:
        config:
        path:
        phi:

    Returns: train_ds: FruitDatasetGenerator, val_ds: FruitDatasetGenerator

    """
    #train_data = get_file_names_for_dataset("trainval", path=path)
    #val_data = get_file_names_for_dataset("trainval", path=path)
    train_data = get_file_names_for_dataset("train", path=path)
    val_data = get_file_names_for_dataset("val", path=path)

    annotations_path = os.path.join(path, "Annotations/")
    image_path = os.path.join(path, "JPEGImages/")

    train_ds = FruitDatasetGenerator(train_data, annotations_path, image_path,
                                     batch_size=config['batch_size'],
                                     image_shape=edet[phi][0])
    val_ds = FruitDatasetGenerator(val_data, annotations_path, image_path,
                                   batch_size=config['batch_size'],
                                   image_shape=edet[phi][0])

    return train_ds, val_ds


def optimizer_from_config(config):
    """

    Args:
        config:

    Returns:

    """
    if config['optimizer'] == 'adam':
        config['optimizer'] = tf.keras.optimizers.Adam

    elif config['optimizer'] == 'rmsprop' or config['optimizer'] == 'RMSprop':
        config['optimizer'] = tf.keras.optimizers.RMSprop

    else:
        warnings.warn('Warning: Invalid Optimizer, defaulting to Adam')
        config['optimizer'] = tf.keras.optimizers.Adam

    return config['optimizer'](learning_rate=config['learning_rate'])


class ReLU6(tf.keras.layers.Layer):
    def __init__(self):
        super(ReLU6, self).__init__()

    def __call__(self, x, *args, **kwargs):
        return tf.keras.layers.ReLU(max_value=6)(x)


def model_from_config(config, phi):
    """ Create model.

    Args:
        config: Dictionary with model configurations.
        phi:

    Returns: Compiled model.

    """
    if config['activations'] == 'relu':
        config['activations'] = tf.keras.layers.ReLU

    elif config['activations'] == 'relu6':
        config['activations'] = ReLU6

    elif config['activations'] == 'swish':
        config['activations'] = Swish

    else:
        warnings.warn('Warning: Invalid Activation, defaulting to Swish')
        config['activations'] = Swish

    efficient_net_params = enet[edet[phi][1]][0:3]
    fpn_params = edet[phi][2:4]
    pred_params = edet[phi][3:5]

    optimizer = optimizer_from_config(config)

    train_model = efficientdet(input_shape=edet[phi][0],
                               enet_params=efficient_net_params,
                               fpn_params=fpn_params, pred_params=pred_params,
                               activation_func=config["activations"])

    train_model.compile(optimizer=optimizer, loss={"regression": smooth_l1,
                                                   "classification":
                                                       focal_loss})

    return train_model


def distributed_training(config, data_dir=None, checkpoint_dir=None):
    """ Runs a distributed training with ray tune to sweep the hyperpameter
    space. Both data_dir and checkpoint_dir don't need to be set, they serve
    internal ray processes.

    Args:
    config (dict): Contains all parameter to initialize the training
    data_dir (string, optional): Path to enable data parlelization
    checkpoint_dir (string, optional): Checkpoint path for ray tune
        defaults to tune.checkpoint_dir()

    Args:
        config (dict): contains all parameter to initialize the training
        data_dir:
        checkpoint_dir:
    """


    train_ds, val_ds = load_data(config, config['path'], config['phi'])
    train_model = model_from_config(config, config['phi'])

    # Mapping from ray tune metric name as key to tensorflow metric name
    metric_dict = {'val_loss': 'val_loss',
                   'val_classification_loss': 'val_classification_loss',
                   'val_regression_loss': 'val_regression_loss',
                   'train_loss': 'loss',
                   'train_classification_loss': 'classification_loss',
                   'mAP': 'mAP',
                   'train_regression_loss': 'regression_loss'}

    callbacks = create_callbacks(train_model, val_ds, config=config, evaluation=True, w_and_b=True)
    callbacks.append(TuneReportCallback(metric_dict))

    with tune.checkpoint_dir(0) as checkpoint_dir:
        model_path = os.path.join(checkpoint_dir, "model_checkpoint")

    cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=model_path,
                                                         save_weights_only=False,
                                                         save_freq='epoch',
                                                         mode='max',
                                                         monitor='mAP',
                                                         verbose=1)

    callbacks.append(cp_callback)
    # Ray Tune handles the number of iterations
    train_model.fit(train_ds, epochs=config['num_epochs'], verbose=0, validation_data=val_ds,
                    callbacks=callbacks)


def create_callbacks(model, val_ds, config, evaluation=False, w_and_b=False,
                     time_measure=False):
    """

    Args:
        val_ds: Validation dataset generator.
        evaluation: Whether to calculate mAP for val_ds or not.
        w_and_b: Log results with w and b.
        time_measure: Measure time.

    Returns:

    """
    callbacks = []

    if evaluation:
        from callbacks.eval import Evaluate
        callbacks.append(Evaluate(generator=val_ds, w_and_b=w_and_b))

    if time_measure:
        pass

    if w_and_b:
        initialize_logging(config)
        callbacks.append(WandbCallback())

    return callbacks


def run_training(config, path, phi, evaluation, w_and_b):
    """Runs an efficient det model with the defined parameters in the
    config

    Args:
        config (dict): contains all parameter to initialize the training
        path:
        phi:
        evaluation:
        w_and_b:
    """

    train_ds, val_ds = load_data(config, path, phi)

    tf.random.set_seed(522)
    np.random.seed(522)

    if config['load_model'] == True:
        train_model = tf.keras.models.load_model('best_model/', custom_objects={'focal_loss': focal_loss, 'smooth_l1': smooth_l1})
        print('Model loaded from disk')

    else:
        train_model = model_from_config(config, phi)

    callbacks = create_callbacks(train_model, evaluation=evaluation, w_and_b=w_and_b,
                                 val_ds=val_ds, config=config)

    cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath='trained_models/',
                                                             save_weights_only=False,
                                                             save_freq='epoch',
                                                             mode='max',
                                                             monitor='mAP',
                                                             verbose=1)

    callbacks.append(cp_callback)


    train_model.fit(train_ds, epochs=config['num_epochs'], verbose=1,
                    validation_data=val_ds, callbacks=callbacks)


def parse_args(args):
    parser = argparse.ArgumentParser(description="Start training script ...")

    parser.add_argument('--dataset_path',
                        help='Path to dataset (ie. /path/to/dataset/).',
                        default='/Users/zeynep068/efficientdet/voc_data/')
    parser.add_argument('--phi',
                        help='Type of EfficientDet (ie. efficientdet-d0).',
                        default="efficientdet-d0")
    parser.add_argument('--batch_size', help='Number of items in the batch.',
                        default=1, type=int)
    parser.add_argument('--epochs', help='Number of epochs for training.',
                        type=int, default=3500)
    parser.add_argument('--evaluation', help='Enable per epoch evaluation.',
                        default='True')
    parser.add_argument('--w_and_b', help='Logs for w and b.', default='False')
    parser.add_argument('--num_tries', help='Number of models to test out',
                        type=int, default=10)
    parser.add_argument('--gpus_per_trial', help='Number of GPU(s) per trial',
                        type=float, default=1)

    parser.add_argument('--load_model', help='Boolean if model should be loaded',
                        default="False")

    # TODO
    parser.add_argument('--save_dir', help='Directory to save trained model.',
                        default="None")
    parser.add_argument('--save_model', help='To save the trained model.',
                        default='False')

    print(vars(parser.parse_args(args)))

    return parser.parse_args(args)


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    args = parse_args(args)

    config = {'optimizer': "adam", 'learning_rate': 5e-4,
              'num_epochs': args.epochs, 'activations': "relu",
              'batch_size': args.batch_size, 'load_model': args.load_model}

    if len(tf.config.experimental.list_physical_devices('GPU')):
        DEVICE = "/gpu:0"
        print("Use GPU")
    else:
        DEVICE = "/cpu:0"
        print("Use CPU")

    with tf.device(DEVICE):
        run_training(config, args.dataset_path, args.phi, args.evaluation,
                     args.w_and_b)


if __name__ == "__main__":
    os.environ['WANDB_API_KEY'] = '3cd8d3bad9089df697ef0cb74e91e6e0d526af89'
    main()
