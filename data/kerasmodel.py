from keras.datasets import mnist
#import matplotlib.pyplot as plt
from keras.utils import to_categorical, plot_model
from keras.models import Model
from keras.layers import Dense, Flatten, Dropout, Conv3D, MaxPooling3D, Input, BatchNormalization


import os
os.environ["PATH"] += os.pathsep + 'C:\\Program Files (x86)\\Graphviz2.38\\bin'


ker = (3, 3, 3)
pool = (2, 2, 2)

#input layer, shape of data to intake specified
input_layer = Input((31, 31, 24, 3))





#first conv and pool
conv_layer1 = Conv3D(filters = 23064, kernel_size = ker, activation  = 'relu', bias_initializer = 'glorot_uniform')(input_layer)
pooling_layer1 = MaxPooling3D(pool_size = pool)(conv_layer1)

#second conv and pool
conv_layer2 = Conv3D(filters = 46128, kernel_size = ker, activation = 'relu', bias_initializer = 'glorot_uniform')(pooling_layer1)
pooling_layer2 = MaxPooling3D(pool_size = pool)(conv_layer2)

#batch normalize
pooling_layer2 = BatchNormalization()(pooling_layer2)
#flatten to transition to dense
flatten_layer = Flatten()(pooling_layer2)


#start dense layers
dense_layer1 = Dense(units = 2048, activation = 'tanh', bias_initializer = 'glorot_uniform')(flatten_layer)
dense_layer1 = Dropout(0.5)(dense_layer1)
dense_layer2 = Dense(units = 1024, activation = 'tanh', bias_initializer = 'glorot_uniform')(dense_layer1)
dense_layer2 = Dropout(0.5)(dense_layer2)
output_layer = Dense(units = 10, activation = 'softmax', bias_initializer = 'glorot_uniform')(dense_layer2)

model = Model(inputs = input_layer, outputs = output_layer)

model.compile(optimizer = 'adadelta', loss = 'categorical_crossentropy', metrics = ['accuracy'])

plot_model(model, to_file = "model.png")


#model.fit(X_train, y_train, validation_data = (X_test, y_test), epochs = 10)
