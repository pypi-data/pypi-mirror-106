from tensorflow.keras.activations import sigmoid
from tensorflow.keras.layers import Layer


class Swish(Layer):
    def __init__(self):
        super(Swish, self).__init__()

    def call(self, x, **kwargs):
        return x * sigmoid(x)
