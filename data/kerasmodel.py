from keras.datasets import mnist
#import matplotlib.pyplot as plt
from keras.utils import to_categorical, plot_model
from keras.models import Model
from keras.layers import Dense, Flatten, Dropout, Conv3D, MaxPooling3D, Input, BatchNormalization
import h5py
import numpy as np


import os
os.environ["PATH"] += os.pathsep + 'C:\\Program Files (x86)\\Graphviz2.38\\bin'
os.chdir('C:/Users/rajes/OneDrive/Documents/ELEC498 numba 2/ELEC-498-Capstone/data')

ker = (3, 3, 3)
pool = (2, 2, 2)



h5f = h5py.File('cleandata.h5', 'r')
b = h5f['dataset_x'][:]
c = h5f['dataset_y'][:]




g = to_categorical(c)

for thing,stuff in zip(g,c):
    print(thing)
    print(stuff)
print(min(c))
print(max(c))



#shuffle the data in unison to get a random test and training set
rng_state = np.random.get_state()
np.random.shuffle(b)
np.random.set_state(rng_state)
np.random.shuffle(g)




#determine indeces of the training data limits
train_amount = int((len(b)*4)/5)


train_x, test_x = b[:train_amount,:], b[train_amount:, :]

train_y, test_y = g[:train_amount,:], g[train_amount:, :]


#following is model definition

#input layer, shape of data to intake specified
input_layer = Input((24, 31, 31, 3))

#first conv and pool
conv_layer1 = Conv3D(filters = 32, kernel_size = ker, activation  = 'relu', bias_initializer = 'glorot_uniform')(input_layer)
pooling_layer1 = MaxPooling3D(pool_size = pool)(conv_layer1)

#second conv and pool
conv_layer2 = Conv3D(filters = 64, kernel_size = ker, activation = 'relu', bias_initializer = 'glorot_uniform')(pooling_layer1)
pooling_layer2 = MaxPooling3D(pool_size = pool)(conv_layer2)

#batch normalize
#pooling_layer2 = BatchNormalization()(pooling_layer2)
#flatten to transition to dense
flatten_layer = Flatten()(pooling_layer2)


#start dense layers
dense_layer1 = Dense(units = 64, activation = 'tanh', bias_initializer = 'glorot_uniform')(flatten_layer)
dense_layer1 = Dropout(0.5)(dense_layer1)
dense_layer2 = Dense(units = 32, activation = 'tanh', bias_initializer = 'glorot_uniform')(dense_layer1)
dense_layer2 = Dropout(0.5)(dense_layer2)
output_layer = Dense(units = 10, activation = 'softmax', bias_initializer = 'glorot_uniform')(dense_layer2)

model = Model(inputs = input_layer, outputs = output_layer)

model.compile(optimizer = 'adadelta', loss = 'categorical_crossentropy', metrics = ['accuracy'])

plot_model(model, to_file = "model.png")


model.fit(train_x, train_y, validation_data = (test_x, test_y), epochs = 10)
