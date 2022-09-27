def affine_rot(model,theta):
    total_acc=0
    n=0
    predictions1 = model.predict(test_dataset)
    images_augmented = []
    labels = []
    cnt = 0
    for image,lab in test_dataset.unbatch():
      if(cnt<1000): 
        tr = tfa.image.rotate(image,theta)
        images_augmented.append(tr)
        labels.append(lab)
        cnt+=1
    labels = np.array(labels)
    images_augmented = tf.stack(images_augmented,0)
    preds1 = model.predict(images_augmented)
    accuracy = tf.reduce_sum(tf.cast(tf.argmax(preds1, axis=-1) == tf.argmax(predictions1[:1000], axis=-1),dtype=tf.int32))
    total_acc+=accuracy
    print(model.evaluate(images_augmented,labels))
    print(model.evaluate(test_dataset))
    
def affine_scale(model,scale,constant):
    total_acc=0
    n=0
    predictions1 = model.predict(test_dataset)
    images_augmented = []
    labels = []
    #image2 =np.array(image2)
    for image,lab in test_dataset.unbatch():
      tr = tfa.image.transform(image,[scale,0.0,-20,0.0,scale,-20,0,0])
      images_augmented.append(tr)
      labels.append(lab)
    #image2 = tf.keras.layers.RandomZoom(0.3,0.3)(test_dataset)
    n+=len(image2)
    images_augmented = tf.stack(images_augmented,0)
    labels = np.array(labels)
    predictions2 = model.predict(images_augmented)
    accuracy = tf.reduce_sum(tf.cast(tf.argmax(predictions2, axis=-1) == tf.argmax(predictions1, axis=-1),dtype=tf.int32))
    total_acc+=accuracy
    print(total_acc/n)
    print(total_acc)
    print(model.evaluate(images_augmented,labels))
    print(model.evaluate(test_dataset))

def affine_shear(model,scale,constant):
    total_acc=0
    n=0
    predictions1 = model.predict(test_dataset)
    images_augmented = []
    labels = []
    #image2 =np.array(image2)
    for image,lab in test_dataset.unbatch():
      tr = tfa.image.transform(image,[1.0,scale,-20,scale,1.0,-20,0,0])
      image2.append(tr)
      labels.append(lab)
    #image2 = tf.keras.layers.RandomZoom(0.3,0.3)(test_dataset)
    n+=len(images_augmented)
    images_augmented = tf.stack(images_augmented,0)
    labels = np.array(labels)
    predictions2 = model.predict(images_augmented)
    accuracy = tf.reduce_sum(tf.cast(tf.argmax(predictions2, axis=-1) == tf.argmax(predictions1, axis=-1),dtype=tf.int32))
    total_acc+=accuracy
    print(total_acc/n)
    print(total_acc)
    print(model.evaluate(images_augmented,labels))
    print(model.evaluate(test_dataset))