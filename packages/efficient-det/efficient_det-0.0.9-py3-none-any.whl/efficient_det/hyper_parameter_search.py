import os
import sys
import numpy as np
import ray
from ray import tune
from ray.tune import CLIReporter
from ray.tune.schedulers import ASHAScheduler

from efficient_det.train import parse_args
from efficient_det.train import distributed_training


def hyper_param_search(config, num_tries=10, gpus_per_trial=1,
                       cpus_per_trial=4):
    """Hyper parameter sweep. Automatically manages resources so all GPUs
    are used. Includes early stopping.

    Args:
        config:
        num_tries: Number of combinations to try
        gpus_per_trial (float): Number of GPU(s) for each trial. Can be 0.5
        cpus_per_trial (int): Number of CPUs for each trial. Defaults to 4.
    """
    # START RAY TUNE IMPORT

    import tensorflow as tf

    tf.compat.v1.enable_eager_execution()
    tf.executing_eagerly()
    tf.random.set_seed(522)
    np.random.seed(522)

    # END OF RAY TUNE IMPORTS

    run_prefix = 'small_space_522_'
    
    strategy = tf.distribute.MirroredStrategy()
    with strategy.scope():
        # Asynchronous Hyperband parameter search algorithm
        # A SYSTEM FOR MASSIVELY PARALLEL HYPERPARAMETER TUNING
        # https://arxiv.org/pdf/1810.05934.pdf

        scheduler = ASHAScheduler(metric="mAP", mode="max", grace_period=3,
                                  reduction_factor=2, max_t=config['num_epochs'])

        # Reports progress as terminal output
        reporter = CLIReporter(
            parameter_columns=["learning_rate", "batch_size", "activations",
                               "optimizer"],
            metric_columns=["train_loss", 'train_classification_loss',
                            'train_regression_loss', "training_iteration"])
        result = tune.run(distributed_training,
                          resources_per_trial={"cpu": cpus_per_trial,
                                               "gpu": gpus_per_trial},
                          config=config, num_samples=num_tries, name=run_prefix,
                          checkpoint_score_attr="min-mAP",
                          scheduler=scheduler, progress_reporter=reporter)

        best_trial = result.get_best_trial("mAP", "max", "last")
        print(f"Best trial config: {best_trial.config}")
        print(f"Best trial final mAP score: {best_trial.last_result['mAP']}")


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    args = parse_args(args)


    config = {'optimizer': 'adam',
              'learning_rate': tune.loguniform(1e-4, 1e-3),
              'num_epochs': args.epochs,
              'activations': tune.choice(['relu', 'relu6']),
              'batch_size': args.batch_size, 'path': args.dataset_path,
              'phi': args.phi, 'evaluation': args.evaluation, 'load_model': False}

    hyper_param_search(config=config, num_tries=args.num_tries,
                       gpus_per_trial=args.gpus_per_trial)
    ray.shutdown()


if __name__ == '__main__':
    #os.environ['WANDB_API_KEY'] = ''
    main()

