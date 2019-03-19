from keras.utils import to_categorical, plot_model
from keras.models import Sequential
from keras.layers import Dense, Flatten, Dropout, Conv3D, MaxPooling3D, Input, BatchNormalization, AveragePooling3D
from keras import optimizers, initializers
import h5py
import numpy as np
from time import time
from keras.callbacks import TensorBoard
import os
import csv
import seaborn as sns
import matplotlib.pyplot as plt

#setting current directories and paths since conda envs interact weird
#specifically add graphviz to path for use with generating model pngs
os.environ["PATH"] += os.pathsep + 'C:\\Program Files (x86)\\Graphviz2.38\\bin'
#set working directory
os.chdir('C:/Users/rajes/OneDrive/Documents/ELEC498renew/ELEC-498-Capstone/data')

#import data from cleaned data file (generated by dataRead.py)
h5f = h5py.File('cleandata.h5', 'r')
b = h5f['dataset_x'][:]
c = h5f['dataset_y'][:]



#convert labels into a one-hot encoded format
g = to_categorical(c)
labels = [0,0,0]
for things in g:
    if np.array_equal(things,[1,0,0]):
        labels[0] += 1
    elif np.array_equal(things,[0,1,0]):
        labels[1] += 1
    elif np.array_equal(things,[0,0,1]):
        labels[2] += 1

sns.barplot(x = [0,1,2], y = labels)
plt.show()


#shuffle the data in unison to get a random test and training set
rng_state = np.random.get_state()
np.random.shuffle(b)
np.random.set_state(rng_state)
np.random.shuffle(g)


#determine indeces of the training data limits
train_amount = int((len(b)*4)/5)

#split training and testing images
train_x, test_x = b[:train_amount,:], b[train_amount:, :]
#split training and testing labels
train_y, test_y = g[:train_amount,:], g[train_amount:, :]


#the following is for testing a singular model
convlayer = 2
denselayer = 4
layersizes = 2048
kernelsize = 3
numepochs = 30
activationfuncs = 'elu'
#construct name




#begin model construction
model = Sequential()


#NAME = "{}-conv-{}-nodes-{}-dense-{}-kernelsize-{}-activation-{}".format(convlayer, layersize, denselayer, kernelsize, funcs, int(time()))
#instantiate tensorboard
#tb = TensorBoard(log_dir="C:\\Users\\rajes\\OneDrive\\Documents\\ELEC498numba2\\ELEC-498-Capstone\\data\\logs/{}".format(NAME))
#print(NAME)   



#add convolution and pooling layers
for i in range(convlayer):
    model.add(Conv3D(filters = 32, kernel_size = (1,kernelsize,kernelsize), strides = (1,1,1), activation  = 'relu', bias_initializer = 'glorot_uniform', input_shape = (24,31,31,3)))
    model.add(MaxPooling3D(pool_size = (2,2,2)))
#add flatten layer
model.add(Flatten())
#add dense layers
#bias = initializers.RandomNormal(mean = 0.5, stddev = 0.05, seed = None)
for i in range(denselayer):
    model.add(Dense(units = layersizes, activation = 'elu', bias_initializer = 'glorot_uniform'))
    model.add(BatchNormalization())
    model.add(Dropout(0.2))
#add output layer
model.add(Dense(units = 3, activation = 'softmax', bias_initializer = 'glorot_uniform'))
#compile model
#create SGD optimizer
sgd = optimizers.SGD(lr = 0.01, clipnorm = 1)
model.compile(optimizer = sgd, loss = 'categorical_crossentropy', metrics = ['accuracy'])

#fit model
model.fit(train_x, train_y, validation_data = (test_x, test_y), epochs = numepochs)
  


                    



