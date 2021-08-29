import tensorflow as tf
# import tensorflow.compat.v1 as tf


# tensorflow安装的是2.6版本已经没有session这个方法了
# sess = tf.Session()
# a = tf.constant(10)
# b = tf.constant(12)
# sess.run(a+b)

# tensorFlow 2.6.0版本
print(tf.add(1, 2).numpy())
hello = tf.constant('Hello, TensorFlow!')
print(hello.numpy())

"""
x_vals = np.random.rand(100).astype(np.float32)
y_vals = x_vals * 8 + 0.01

weight = tf.Variable(tf.random_uniform_initializer([1]))
biase = tf.Variable(tf.zeros[1])
y = x_vals * weight + biase

loss = tf.reduce_mean(tf.square(y - y_vals))
optimizer = tf.train.GradientDescentOptimizer(0.5)
"""
