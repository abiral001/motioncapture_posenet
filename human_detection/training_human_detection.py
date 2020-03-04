import numpy as np
import os
import tensorflow as tf
from tensorflow.keras.models import load_model, Sequential
from tensorflow.keras.layers import Conv2D, MaxPool2D, Dropout
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import TensorBoard
from tensorflow.keras.layers import LeakyReLU

X_train = np.load('X_train.npy')
X_val = np.load('X_val.npy')
y_train = np.load('y_train.npy')
y_val = np.load('y_val.npy')

X_train = X_train/255.
X_val = X_val/255.

y_train = to_categorical(y_train, dtype = int)
y_val = to_categorical(y_val, dtype = int)

tf_cb = TensorBoard(log_dir='human_detection\\', profile_batch=100000000)

#building the model

model = Sequential()
model.add(Conv2D(128, kernel_size = 3, input_shape = (80, 80, 1)))
model.add(LeakyReLU(alpha = 0.01))
model.add(MaxPool2D(5))
model.add(Dropout(0.5))

model.add(Conv2D(256, kernel_size = 3))
model.add(LeakyReLU(alpha = 0.01))
model.add(MaxPool2D(5))
model.add(Dropout(0.5))

model.add(Flatten())
model.add(Dense(1000))
model.add(LeakyReLU(alpha = 0.01))

model.add(Dense(2, activation = 'softmax'))

adda = Adam(learning_rate = 0.01)

model.compile(optimizer=adda, loss = 'categorical_crossentropy', metrics = ['accuracy'])

model.fit(X_train, y_train, batch_size = 200, epochs = 50, callbacks = [tf_cb], validation_data = (X_val, y_val))

model.save('Human_detection.keras')