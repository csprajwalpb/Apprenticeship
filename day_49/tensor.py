import tensorflow as tf

# Example 1: Scalar addition
a = tf.constant(5)
b = tf.constant(3)
c = tf.add(a, b)  # or simply a + b
print("1. Scalar addition:", c.numpy())  # 8

# Example 2: Scalar subtraction
d = tf.subtract(a, b)  # or a - b
print("2. Scalar subtraction:", d.numpy())  # 2

# Example 3: Scalar multiplication
e = tf.multiply(a, b)  # or a * b
print("3. Scalar multiplication:", e.numpy())  # 15

# Example 4: Scalar division
f = tf.divide(a, b)  # note: gives float
print("4. Scalar division:", f.numpy())  # ~1.6667

# Example 5: Element-wise operations on vectors
v1 = tf.constant([1, 2, 3], dtype=tf.float32)
v2 = tf.constant([4, 5, 6], dtype=tf.float32)
add_v = v1 + v2  # element-wise addition
sub_v = v1 - v2
mul_v = v1 * v2
div_v = v1 / v2
print("5. Vector operations:")
print("   add:", add_v.numpy())     # [5, 7, 9]
print("   subtract:", sub_v.numpy())# [-3, -3, -3]
print("   multiply:", mul_v.numpy())# [4, 10, 18]
print("   divide:", div_v.numpy())  # [0.25, 0.4, 0.5]

# Example 6: Matrix addition
m1 = tf.constant([[1, 2], [3, 4]], dtype=tf.int32)
m2 = tf.constant([[5, 6], [7, 8]], dtype=tf.int32)
m_add = m1 + m2
print("6. Matrix addition:\n", m_add.numpy())  # [[6,8],[10,12]]

# Example 7: Element-wise matrix multiplication
m_mul = tf.multiply(m1, m2)
print("7. Element-wise matrix multiplication:\n", m_mul.numpy())  # [[5,12],[21,32]]

# Example 8: Matrix multiplication (dot product)
m_matmul = tf.matmul(m1, m2)
print("8. Matrix multiplication (matmul):\n", m_matmul.numpy())
# This is standard matrix multiplication, not element-wise.

# Example 9: Reduce sum (sum all elements)
sum_all = tf.reduce_sum(m1)
print("9. Sum of all elements in m1:", sum_all.numpy())  # 1+2+3+4 = 10

# Example 10: Scalar multiply tensor (scale a tensor by a scalar)
scalar = tf.constant(10, dtype=tf.int32)
scaled = tf.math.scalar_mul(scalar, m1)  # multiply each element by 10 :contentReference[oaicite:0]{index=0}
print("10. Scalar * tensor:\n", scaled.numpy())  # [[10,20],[30,40]]