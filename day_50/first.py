import tensorflow as tf
import numpy as np
print('TensorFlow Version:', tf.__version__)

x=tf.Variable(10)
x
v=tf.Variable([1,2,3]); v
m=tf.Variable([[1.0,2.0],[3.0,4.0]]); m
w=tf.Variable(tf.random.normal([3,3])); w
x=tf.Variable(5); x.assign(20); x
x=tf.Variable(5); x.assign_add(10); x
x=tf.Variable(30); x.assign_sub(5); x
W=tf.Variable(tf.random.normal([4,2])); W
b=tf.Variable(tf.zeros([2])); b