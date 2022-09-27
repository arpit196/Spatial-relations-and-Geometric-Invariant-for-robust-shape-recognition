import tensorflow as tf
import tensorflow_datasets as tfds
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras import layers

#This function extracts the local second derivative features (curvature) from object boundaries and contours.
#Multiple successive operations give higher order derivates such as nth order derivative information.
def LocalCurvature(input_tensor):
  filter = tf.constant([[[-1.0,0.0],[1.0,0.0]],[[0.0,0.0],[1.0,-1.0]]])
  filter = filter[:,:,tf.newaxis]
  filter = tf.tile(filter,[1,1,1,1])
  out = tf.nn.conv2d(input_tensor, filters=filter,padding="SAME",strides=[1, 3, 3, 1])
  return out
 
#This function encodes the relative locations between parts.
def relative_locations(q, k):
    q = tf.cast(q,dtype=tf.float32)
    k = tf.cast(k,dtype=tf.float32)
    dim = q.shape[1]
    dim2 = q.shape[3]
    q = tf.reshape(q,[-1,dim*dim,dim2])[:,:,:,tf.newaxis]
    k = tf.reshape(k,[-1,dim*dim,dim2])[:,:,:,tf.newaxis]
    q = tf.where(q>0,q,0)
    k = tf.where(k>0,k,0)
    q = layers.Dense(dim2,activation='relu')(q)
    k = layers.Dense(dim2,activation='relu')(k)
    dist = tf.transpose(q,[0,1,3,2]) - tf.transpose(k,[0,1,2,3])
    pairwise_euclidean_distance = tf.reduce_sum(tf.math.square(dist),2)
    print(pairwise_euclidean_distance.shape)
    pairwise_euclidean_distance = tf.math.l2_normalize(pairwise_euclidean_distance,axis=-1)
    pairwise_euclidean_distance = tf.reshape(pairwise_euclidean_distance,[-1,dim,dim,dim2])
    return pairwise_euclidean_distance