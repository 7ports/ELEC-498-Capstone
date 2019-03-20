from keras.utils import to_categorical
from keras.models import load_model
import h5py
import numpy as np
import os


#set working directory
os.chdir('C:/Users/rajes/OneDrive/Documents/ELEC498renew/ELEC-498-Capstone/data')
model  = load_model("C:\\Users\\rajes\\OneDrive\\Documents\\ELEC498renew\\ELEC-498-Capstone\\data\\2-conv-2048-nodes-4-dense-3-kernelsize-elu-activation-1553007335.hdf5")


h5f = h5py.File('cleandata.h5', 'r')
b = h5f['dataset_x'][:]
c = h5f['dataset_y'][:]




g = to_categorical(c)
predictions = model.predict(b,batch_size = None, verbose = 1, steps = None)
for i in range(len(predictions)):
    for j in range(3):
        if predictions[i][j] == max(predictions[i]):
            predictions[i][j] = 1
        else:
            predictions[i][j] = 0

count = 0
for i in range(len(predictions)):
    if np.array_equal(predictions[i], g[i]):
        count += 1
total = len(predictions)
print(count/total)