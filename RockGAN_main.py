import os

os.environ["KERAS_BACKEND"] = "jax"

import keras, jax
print("Keras backend:", keras.backend.backend())
print("JAX devices:", jax.devices())