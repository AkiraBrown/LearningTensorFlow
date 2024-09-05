import tensorflow as tf
print(tf.__version__)
string = tf.Variable("this is a string", tf.string)
number = tf.Variable(324, tf.int16)
floating = tf.Variable(3.567, tf.float64)

print(string,number,floating)