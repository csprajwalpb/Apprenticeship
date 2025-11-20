import tensorflow as tf
import numpy as np
print('TensorFlow Version:', tf.__version__)

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

x=tf.placeholder(tf.int32); y=x*2
sess=tf.Session(); sess.run(y,{x:10})
x=tf.placeholder(tf.float32,shape=[3]); sess=tf.Session(); sess.run(x,{x:[1,2,3]})
x=tf.placeholder(tf.float32,shape=[2,2]); sess=tf.Session(); sess.run(x,{x:[[10,20],[30,40]]})
a=tf.placeholder(tf.int32); b=tf.placeholder(tf.int32); c=a+b
sess=tf.Session(); sess.run(c,{a:20,b:30})
x=tf.placeholder(tf.float32,shape=[None,784]); 'MNIST placeholder created'
y=tf.placeholder(tf.int32,shape=[None,10]); 'Label placeholder created'
keep=tf.placeholder(tf.float32); 'Dropout placeholder created'
x=tf.placeholder(tf.float32); y=tf.placeholder(tf.float32); z=x+y
sess=tf.Session(); sess.run(z,{x:3.5,y:4.5})
x=tf.placeholder(tf.float32,shape=[None,28,28]); '3D placeholder created'
x=tf.placeholder(tf.float32,shape=[None,3])
W=tf.Variable(tf.random.normal([3,2])); b=tf.Variable(tf.zeros([2]))
y=tf.matmul(x,W)+b
sess=tf.Session(); sess.run(tf.global_variables_initializer()); sess.run(y,{x:[[1,2,3]]})