from keras.utils import to_categorical
from keras.models import load_model
import h5py
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
import csv

#set working directory
os.chdir('C:/Users/rajes/OneDrive/Documents/ELEC498renew/ELEC-498-Capstone/data')
model  = load_model("F:/ELEC498modelskernels/2-conv-2048-nodes-3-dense-3-kernelsize-elu-activation-0.1-dropoutrate-0.01-learningrate-timestamp-1553721359/2-conv-2048-nodes-3-dense-3-kernelsize-elu-activation-0.1-dropoutrate-0.01-learningrate-timestamp-1553721359.h5")


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


things = [0,0,0]

for i in range(len(predictions)):
    for j in range(3):
        if predictions[i][j] == 1:
            things[j] += 1

sns.barplot(x = [0,1,2], y = things)
plt.xlabel("Class Labels", fontsize = 20)
plt.ylabel("Number of Samples", fontsize = 20)
plt.title("Model Predictions", fontsize = 25)
plt.show()
"""
xt = []
yt = []
for i in range(10):
    xt.append(i)

with open("thingy.csv", 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        yt.append(int(row[1]))

print(xt)
print(yt)
sns.barplot(x = xt, y = yt)
plt.xlabel("Class Labels", fontsize = 20)
plt.ylabel("Number of Samples", fontsize = 20)
plt.title("Data Distribution", fontsize = 25)
plt.show()
"""