import sys
import tensorflow as tf
import sklearn

print("Python executable:")
print(sys.executable)
print()

print("TensorFlow version:", tf.__version__)
print("Scikit-learn version:", sklearn.__version__)
print("GPUs:", tf.config.list_physical_devices("GPU"))
