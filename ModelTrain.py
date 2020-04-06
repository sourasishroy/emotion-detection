import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D,MaxPooling2D, BatchNormalization
from tensorflow.keras.callbacks import TensorBoard,ReduceLROnPlateau
from tensorflow.keras.regularizers import l2
import numpy as np
from tensorflow.keras.utils import to_categorical
import time
#2-64-0 3-64-0 4-64-0 4-128-1 4-64-2 4-128-2
name="EmotionDetection-{}".format(int(time.time()))
tensorboard=TensorBoard(log_dir='logs\{}'.format(name))
X_test=np.load("test_X.npy")
Y_test=np.load("test_Y.npy")
X_train=np.load("train_X.npy")
Y_train=np.load("train_Y.npy")

Y_train=Y_train.reshape(Y_train.shape[0],1)
Y_test=Y_test.reshape(Y_test.shape[0],1)

X_test/=255.0
X_train/=255.0

Y_train=to_categorical(Y_train, num_classes=7)
Y_test=to_categorical(Y_test, num_classes=7)

model.add(Conv2D(64, (3, 3), activation='relu', input_shape=(48, 48, 1), kernel_regularizer=l2(0.01)))
model.add(Conv2D(64, (3, 3), padding='same',activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2), strides=(2, 2)))
model.add(Dropout(0.1))

model.add(Conv2D(128, (3, 3), padding='same', activation='relu'))
model.add(BatchNormalization())

model.add(Conv2D(128, (3, 3), padding='same', activation='relu'))
model.add(BatchNormalization())

model.add(Conv2D(128, (3, 3), padding='same', activation='relu'))
model.add(BatchNormalization())

model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.1))

model.add(Conv2D(256, (3, 3), padding='same', activation='relu'))
model.add(BatchNormalization())

model.add(Conv2D(256, (3, 3), padding='same', activation='relu'))
model.add(BatchNormalization())

model.add(Conv2D(256, (3, 3), padding='same', activation='relu'))
model.add(BatchNormalization())

model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.1)) 

model.add(Conv2D(512, (3, 3), padding='same', activation='relu'))
model.add(BatchNormalization())

model.add(Conv2D(512, (3, 3), padding='same', activation='relu'))
model.add(BatchNormalization())

model.add(Conv2D(512, (3, 3), padding='same', activation='relu'))
model.add(BatchNormalization())

model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.1))    
model.add(Flatten())

model.add(Dense(512, activation='relu'))
model.add(Dropout(0.1))

model.add(Dense(256, activation='relu'))
model.add(Dropout(0.1))

model.add(Dense(128, activation='relu'))
model.add(Dropout(0.1))

model.add(Dense(64, activation='relu'))
model.add(Dropout(0.1))

model.add(Dense(7, activation='softmax'))

model.compile(loss='categorical_crossentropy',optimizer="adam", metrics=['accuracy'])

model.fit(X_train,Y_train,batch_size=64,validation_data=(X_test,Y_test), epochs=150,callbacks=[tensorboard])

