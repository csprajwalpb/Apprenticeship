# ================================
# SECTION B — TensorFlow Variables
# ================================

import tensorflow as tf

print("TensorFlow Version:", tf.__version__)


# --------------------------------
# 1️⃣ Bank Account Balance Update
# --------------------------------
balance = tf.Variable(5000.0)
salary = 1500.0

for month in range(6):
    balance.assign(balance + salary)

print("\n1) Final Bank Balance:", balance.numpy())


# --------------------------------
# 2️⃣ Training Weight Update
# --------------------------------
weight = tf.Variable(5.0)
gradient = 2.0
learning_rate = 0.1

new_weight = weight - learning_rate * gradient
weight.assign(new_weight)

print("\n2) Updated Weight:", weight.numpy())


# --------------------------------
# 3️⃣ Counter Variable
# --------------------------------
count = tf.Variable(0)

for i in range(10):
    count.assign_add(1)

print("\n3) Final Counter Value:", count.numpy())


# --------------------------------
# 4️⃣ Temperature Monitoring
# --------------------------------
temperature = tf.Variable(25.0)
increments = [1, -2, 3, 0, 4]

for inc in increments:
    temperature.assign_add(inc)

print("\n4) Final Temperature:", temperature.numpy())


# --------------------------------
# 5️⃣ Stock Price Fluctuation
# --------------------------------
stock = tf.Variable(100.0)
changes = [0.05, -0.03, 0.02]  # % changes

for ch in changes:
    stock.assign(stock * (1 + ch))

print("\n5) Final Stock Price:", stock.numpy())


# --------------------------------
# 6️⃣ Model Bias Training
# --------------------------------
bias = tf.Variable(0.0)
corrections = [0.3, -0.1, 0.05]

for corr in corrections:
    bias.assign_add(corr)

print("\n6) Final Bias:", bias.numpy())


# --------------------------------
# 7️⃣ Accumulator Variable
# --------------------------------
acc = tf.Variable(0)
values = tf.constant([4, 8, 12, 16], dtype=tf.int32)

for v in values:
    acc.assign_add(v)

print("\n7) Accumulator Final Value:", acc.numpy())


# --------------------------------
# 8️⃣ 2×2 Matrix Variable Update
# --------------------------------
matrix = tf.Variable([[1, 2],
                      [3, 4]], dtype=tf.int32)

update = tf.constant([[1, 1],
                      [1, 1]])

matrix.assign(matrix + update)
print("\n8) Updated Matrix:\n", matrix.numpy())


# --------------------------------
# 9️⃣ Variable Learning Rate Decay
# --------------------------------
learning_rate = tf.Variable(0.1)
decay = 0.95

for epoch in range(4):
    learning_rate.assign(learning_rate * decay)

print("\n9) Learning Rate After 4 Epochs:", learning_rate.numpy())


# --------------------------------
# 🔟 Neural Network Weight Initialization
# --------------------------------
weights = tf.Variable(tf.random.normal((3, 3)))

mean = tf.reduce_mean(weights)
stddev = tf.math.reduce_std(weights)

print("\n10) Weight Matrix:\n", weights.numpy())
print("Mean:", mean.numpy())
print("Std Dev:", stddev.numpy())
