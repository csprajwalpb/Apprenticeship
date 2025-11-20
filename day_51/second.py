import tensorflow as tf
import numpy as np
print('TensorFlow Version:', tf.__version__)

c=tf.constant(10); c
c=tf.constant(3.14); c
c=tf.constant([1,2,3]); c
c=tf.constant([[1,2],[3,4]]); c
c=tf.constant([1,2,3],dtype=tf.float32); c
a=tf.constant(5); b=tf.constant(7); a+b
a=tf.constant(4); b=tf.constant(8); a*b
a=tf.constant([1,2,3]); b=tf.constant([4,5,6]); tf.tensordot(a,b,1)
I=tf.eye(4); I
x=tf.constant(8); y=3*x+2; y