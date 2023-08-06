import math
import warnings
import tensorflow as tf

from efficient_det.layers.activation_layer import Swish, ReLU6


def round_filters(width_coefficient, filters, depth_divisor=8.0):
    """ Round number of filters based on width coefficient.

    Args:
        width_coefficient: Coefficient to scale network width.
        filters: Number of filters for a given layer.
        depth_divisor: Constant.

    From tensorflow implementation:
    https://github.com/tensorflow/tpu/blob/master/models/official/efficientnet
    /efficientnet_model.py
    """
    filters *= width_coefficient
    new_filters = int(filters + depth_divisor / 2)
    new_filters = new_filters // depth_divisor * depth_divisor
    new_filters = max(depth_divisor, new_filters)

    # Make sure that round down does not go down by more than 10%.
    if new_filters < 0.9 * filters:
        new_filters += depth_divisor

    return int(new_filters)


def round_repeats(depth_coefficient, repeats):
    """ Round number of filters based on depth coefficient.

    Args:
        depth_coefficient: Coefficient to scale number of repeats.
        repeats: Number to repeat mb_conv_block.

    From tensorflow implementation:
    https://github.com/tensorflow/tpu/blob/master/models/official/efficientnet
    /efficientnet_model.py

    """
    return int(math.ceil(depth_coefficient * repeats))


def optimizer_from_config(config):
    """ Parse string to optimizer.

    Args:
        config: Includes all model and run settings.
    """
    if config['optimizer'] == 'adam':
        config['optimizer'] = tf.keras.optimizers.Adam

    elif config['optimizer'] == 'rmsprop' or config['optimizer'] == 'RMSprop':
        config['optimizer'] = tf.keras.optimizers.RMSprop

    else:
        warnings.warn('Warning: Invalid Optimizer, defaulting to Adam')
        config['optimizer'] = tf.keras.optimizers.Adam

    return config['optimizer'](learning_rate=config['learning_rate'])


def activation_from_config(config):
    """ Parse string to activation.

    Args:
        config: Includes all model and run settings.
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

    return config['activations']
