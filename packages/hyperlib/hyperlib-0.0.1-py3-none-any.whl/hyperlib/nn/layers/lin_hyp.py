import tensorflow as tf
from tensorflow import keras


class LinearHyperbolic(keras.layers.Layer):
    """
    Implementation of a hyperbolic linear layer for a neural network, that inherits from the keras Layer class
    """

    def __init__(self, units, manifold, c, activation=None):
        super().__init__()
        self.units = units
        # TODO make curavature 'self.c' a learnable parameter
        self.c = tf.constant(c, dtype="float64")
        self.manifold = manifold
        self.activation = keras.activations.get(activation)

    def init_weights_matrix(self, input_shape, irange=1e-5):
        """
        Custom weight matrix initialisation for this layer
        """
        weights = tf.random.uniform(
            shape=[input_shape[-1], self.units],
            minval=-irange,
            maxval=irange,
            dtype=tf.float64,
        )
        return weights

    def build(self, batch_input_shape):
        weight_matrix = self.init_weights_matrix(batch_input_shape)
        self.kernel = tf.Variable(
            initial_value=weight_matrix, dtype="float64", trainable=True,
        )
        # TODO: add bias functionality
        # self.bias = self.add_weight(name="bias", shape=[self.units],initializer="zeros")
        super().build(batch_input_shape)  # must be at the end

    def call(self, inputs):
        """
        Called during forward pass of a neural network. Uses hyperbolic matrix multiplication
        """
        # TODO: remove casting and instead recommend setting default tfd values to float64
        inputs = tf.cast(inputs, tf.float64)
        mv = self.manifold.mobius_matvec(self.kernel, inputs, self.c)
        res = self.manifold.proj(mv, self.c)
        return self.activation(res)

    def get_config(self):
        base_config = super().get_config()
        return {
            **base_config,
            "units": self.units,
            "activation": keras.activations.serialize(self.activation),
        }
