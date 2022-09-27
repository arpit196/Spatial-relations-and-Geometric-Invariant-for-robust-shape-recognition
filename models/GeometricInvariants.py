from keras.engine import keras_tensor
def SingleCurvatureModel():
  inputs = layers.Input(shape=(96, 96, 5))
  
  x_theta = inputs[:,:,:,2]
  x_theta = tf.expand_dims(x1,-1)
  x_theta = tf.tile(x1,[1,1,1,2])
  xc = LocalCurvature(x_theta)
  xc=layers.LayerNormalization()(xc)
  xc2 = LocalCurvature(layers.AveragePooling2D((3,3),strides=1,padding="SAME")(x_theta))
  xc3 = LocalCurvature(layers.AveragePooling2D((5,5),strides=1,padding="SAME")(x_theta))

  xct = layers.Concatenate()([xc,layers.AveragePooling2D(3,3)(inputs)])
  xl = layers.Dense(256,activation='relu')(xct)
  xl = layers.LayerNormalization()(xl)
  xl = layers.Dense(256,activation='relu')(xl)
  
  xl2g = layers.Concatenate()([layers.GlobalMaxPooling2D()(xl)])

  xl2g = layers.BatchNormalization()(xl2g)
  xm = layers.Dense(1024,activation='relu')(xl2g)
  x = layers.Dense(1024,activation='relu')(xm)
  x = layers.Dense(5,activation='softmax')(x)
  return tf.keras.Model(inputs = inputs,outputs = x)