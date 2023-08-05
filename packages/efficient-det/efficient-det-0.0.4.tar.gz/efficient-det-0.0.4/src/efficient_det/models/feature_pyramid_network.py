import tensorflow as tf

from numpy.random import seed
from tensorflow.keras.layers import (Conv2D, UpSampling2D, MaxPooling2D,
                                     AveragePooling2D, Add, DepthwiseConv2D,
                                     ReLU, BatchNormalization)

tf.compat.v1.enable_eager_execution()
tf.executing_eagerly()

seed(1)
tf.random.set_seed(2)


def conv_layer(c, num, kernel_size=1, strides=1):
    """

    Args:
        c:
        num:
        kernel_size:
        strides:

    Returns:

    """
    return Conv2D(filters=num, kernel_size=kernel_size, strides=strides,
                  padding="same", use_bias=True)(c)


def top_down_fusion(p_in, p_top_down, kernel_size=3, strides=1,
                    fuse_nodes=True):
    """ Fuse two nodes on the top down path of the feature network.

    Args:
        p_in:
        p_top_down:
        kernel_size: Kernel size.
        strides: Stride value.
        fuse_nodes: True if node has two incoming nodes.

    Returns:

    """
    if fuse_nodes:
        p_in = depth_block(x=p_in, kernel_size=kernel_size, strides=strides)
    return up_sampling(p_in, size=2) + p_top_down


def up_sampling(p, size=2):
    """

    Args:
        p:
        size:

    Returns:

    """
    return UpSampling2D(size=size, interpolation="nearest")(p)


def down_sampling(p, size=2):
    """

    Args:
        p:
        size:

    Returns:

    """
    return MaxPooling2D(pool_size=2, strides=size, padding="same")(p)


def de_aliasing(x, num):
    """

    Args:
        x:
        num:

    Returns:

    """
    return Conv2D(filters=num, kernel_size=3, padding="same", use_bias=True)(x)


def bottom_up_fusion(p_bottom_up, p_in, p_in_prime=0.0, kernel_size=3,
                     strides=1):
    """

    Args:
        p_bottom_up:
        p_in:
        p_in_prime:
        kernel_size:
        strides:

    Returns:

    """
    p_bottom_up = depth_block(p_bottom_up, kernel_size=kernel_size,
                              strides=strides)
    p_bottom_up = down_sampling(p_bottom_up, size=2)

    return p_bottom_up + p_in_prime + p_in


def depth_wise_conv(p, kernel_size=3, strides=1):
    """

    Args:
        p:
        kernel_size:
        strides:

    Returns:

    """
    conv = DepthwiseConv2D(kernel_size=kernel_size, strides=strides,
                           padding="same", use_bias=False)(p)
    return conv


def depth_block(x, kernel_size=3, strides=1):
    """

    Args:
        x:
        kernel_size:
        strides:

    Returns:

    """
    x = depth_wise_conv(x, kernel_size=kernel_size, strides=strides)
    x = BatchNormalization(axis=3, trainable=False)(x)
    return ReLU()(x)


def create_feature_network(backbone_layers, depth=3, num_features=64):
    """ Create feature pyramid network.

    Args:
        backbone_layers: Use EfficientNetB0 layers.
        num_features: Num channels to project.
        depth: Number of repeats.

    Returns: List of feature maps with different feature map size.

    """
    for i in range(depth):
        if i == 0:
            _, _, p3_in, p4_in, p5_in = backbone_layers
            p3_in = conv_layer(p3_in, num=num_features)
            p4_in = conv_layer(p4_in, num=num_features)
            p5_in = conv_layer(p5_in, num=num_features)
            p6_in = conv_layer(p5_in, num=num_features, kernel_size=3, strides=2)
            p7_in = conv_layer(p6_in, num=num_features, kernel_size=3, strides=2)
        else:
            p3_in, p4_in, p5_in, p6_in, p7_in = backbone_layers
            p3_in = conv_layer(p3_in, num=num_features)
            p4_in = conv_layer(p4_in, num=num_features)
            p5_in = conv_layer(p5_in, num=num_features)
            p6_in = conv_layer(p6_in, num=num_features)
            p7_in = conv_layer(p7_in, num=num_features)

        p6_prime = top_down_fusion(p7_in, p6_in)
        p5_prime = top_down_fusion(p6_prime, p5_in)
        p4_prime = top_down_fusion(p5_prime, p4_in)
        p3_out = top_down_fusion(p4_prime, p3_in)

        p4_out = bottom_up_fusion(p3_out, p4_in, p4_prime)
        p5_out = bottom_up_fusion(p4_out, p5_in, p5_prime)
        p6_out = bottom_up_fusion(p5_out, p6_in, p6_prime)
        p7_out = bottom_up_fusion(p6_out, p7_in)
        p7_out = depth_block(p7_out)

        backbone_layers = p3_out, p4_out, p5_out, p6_out, p7_out

    return backbone_layers
