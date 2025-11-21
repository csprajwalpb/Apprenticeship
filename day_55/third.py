# ================================
# SECTION C — TensorFlow Placeholders
# ================================

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

import numpy as np

print("TensorFlow Version:", tf.__version__)


# --------------------------------
# 1️⃣ Dynamic Addition
# --------------------------------
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

z = x + y

with tf.Session() as sess:
    print("\n1) x + y =", sess.run(z, feed_dict={x: 10, y: 5}))


# --------------------------------
# 2️⃣ Multiply by User Input
# --------------------------------
n = tf.placeholder(tf.float32)
expr = n**2 + n**3

with tf.Session() as sess:
    print("\n2) n^2 + n^3 =", sess.run(expr, feed_dict={n: 3}))


# --------------------------------
# 3️⃣ Student Marks Input (None, 3)
# --------------------------------
marks = tf.placeholder(tf.float32, shape=[None, 3])
averages = tf.reduce_mean(marks, axis=1)

sample_marks = [[80, 90, 70],
                [60, 75, 85]]

with tf.Session() as sess:
    print("\n3) Student Averages:", sess.run(averages, feed_dict={marks: sample_marks}))


# --------------------------------
# 4️⃣ Matrix Multiplication
# --------------------------------
A = tf.placeholder(tf.float32, shape=[2, 2])
B = tf.placeholder(tf.float32, shape=[2, 2])

C = tf.matmul(A, B)

with tf.Session() as sess:
    result = sess.run(C, feed_dict={
        A: [[1, 2], [3, 4]],
        B: [[5, 6], [7, 8]]
    })
    print("\n4) Matrix Multiplication:\n", result)


# --------------------------------
# 5️⃣ Cost Function Evaluation
# --------------------------------
x_ph = tf.placeholder(tf.float32)
cost = 0.5 * x_ph**2 + 2 * x_ph + 5

with tf.Session() as sess:
    print("\n5) Cost Function C(x):", sess.run(cost, feed_dict={x_ph: 4}))


# --------------------------------
# 6️⃣ Feed Batch Data (None, 4)
# --------------------------------
batch = tf.placeholder(tf.float32, shape=[None, 4])
row_sums = tf.reduce_sum(batch, axis=1)

batch1 = np.array([[1,2,3,4],[5,6,7,8]])
batch2 = np.array([[2,4,6,8],[1,3,5,7],[9,9,9,9]])

with tf.Session() as sess:
    print("\n6) Batch 1 Row Sums:", sess.run(row_sums, feed_dict={batch: batch1}))
    print("6) Batch 2 Row Sums:", sess.run(row_sums, feed_dict={batch: batch2}))


# --------------------------------
# 7️⃣ Placeholder for ReLU
# --------------------------------
vec = tf.placeholder(tf.float32)
relu_output = tf.nn.relu(vec)

with tf.Session() as sess:
    print("\n7) ReLU Output:", sess.run(relu_output, feed_dict={vec: [-2, 1, 0, 5]}))


# --------------------------------
# 8️⃣ Polynomial Evaluation
# --------------------------------
x_poly = tf.placeholder(tf.float32)
poly = 3*x_poly**3 - 2*x_poly**2 + 5*x_poly - 7

with tf.Session() as sess:
    print("\n8) Polynomial f(2):", sess.run(poly, feed_dict={x_poly: 2}))


# --------------------------------
# 9️⃣ Image Reshaping (None, 28×28)
# --------------------------------
img = tf.placeholder(tf.float32, shape=[None, 28, 28])
reshaped = tf.reshape(img, [-1, 28, 28, 1])

dummy_img = np.zeros((2, 28, 28))  # 2 images

with tf.Session() as sess:
    result_shape = sess.run(reshaped, feed_dict={img: dummy_img}).shape
    print("\n9) Reshaped Image Shape:", result_shape)


# --------------------------------
# 🔟 Logistic (Sigmoid) Function
# --------------------------------
x_sig = tf.placeholder(tf.float32)
sigmoid = 1 / (1 + tf.exp(-x_sig))

with tf.Session() as sess:
    print("\n10) Sigmoid Output:", sess.run(sigmoid, feed_dict={x_sig: [-2, 0, 2]}))
