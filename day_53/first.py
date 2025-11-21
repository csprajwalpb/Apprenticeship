# ================================
# SECTION A — TensorFlow Constants
# ================================

import tensorflow as tf

print("TensorFlow Version:", tf.__version__)

# --------------------------------
# 1️⃣ Temperature Conversion Constant
# --------------------------------
celsius = tf.constant([0.0, 25.0, 37.0, 100.0], dtype=tf.float32)
factor = tf.constant(1.8)
offset = tf.constant(32.0)

fahrenheit = celsius * factor + offset
print("\n1) Fahrenheit values:", fahrenheit.numpy())

# --------------------------------
# 2️⃣ Area of a Circle
# --------------------------------
pi = tf.constant(3.14159)
radii = tf.constant([2.0, 5.0, 10.0])

area = pi * tf.square(radii)
print("\n2) Areas of circles:", area.numpy())

# --------------------------------
# 3️⃣ Matrix Addition for Images
# --------------------------------
brightness = tf.constant([[10, 10], [10, 10]])
image = tf.constant([[120, 130], [140, 150]])

bright_image = image + brightness
print("\n3) Brightened Image:\n", bright_image.numpy())

# --------------------------------
# 4️⃣ Physics: Speed Calculation
# --------------------------------
distance = tf.constant(150.0)
time = tf.constant(3.0)

speed = distance / time
print("\n4) Speed (km/hr):", speed.numpy())

# --------------------------------
# 5️⃣ Financial GST Calculation
# --------------------------------
gst_rate = tf.constant(0.18)
amounts = tf.constant([1000.0, 1500.0, 2200.0])

final_billing = amounts + amounts * gst_rate
print("\n5) Final Billing Amounts:", final_billing.numpy())

# --------------------------------
# 6️⃣ Constant String Tensor
# --------------------------------
str1 = tf.constant("Tensor")
str2 = tf.constant("Flow")

concat_str = tf.strings.join([str1, str2])
print("\n6) Concatenated String:", concat_str.numpy().decode())

# --------------------------------
# 7️⃣ Sum of First 100 Natural Numbers
# --------------------------------
numbers = tf.constant(range(1, 101))
total_sum = tf.reduce_sum(numbers)
print("\n7) Sum of first 100 natural numbers:", total_sum.numpy())

# --------------------------------
# 8️⃣ Vector Normalization
# --------------------------------
vec = tf.constant([3.0, 4.0])
magnitude = tf.norm(vec)
unit_vec = vec / magnitude

print("\n8) Normalized Vector:", unit_vec.numpy())

# --------------------------------
# 9️⃣ Grayscale to RGB Conversion
# --------------------------------
g = tf.constant(120)
rgb = tf.stack([g, g, g])

print("\n9) Grayscale to RGB:", rgb.numpy())

# --------------------------------
# 🔟 Batch of Student Scores
# --------------------------------
scores = tf.constant([[81, 75, 92],
                      [66, 88, 79]])

row_avg = tf.reduce_mean(scores, axis=1)
col_max = tf.reduce_max(scores, axis=0)

print("\n10) Row-wise Average:", row_avg.numpy())
print("10) Column-wise Max:", col_max.numpy())
