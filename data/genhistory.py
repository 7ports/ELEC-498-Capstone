import pickle
import os
import matplotlib.pyplot as plt
import seaborn as sns
from keras.models import load_model
from keras.utils import to_categorical
import h5py
import numpy as np


colors = ["blue", "gold", "red", "navy blue"]
#preform walk and save in a variable
walked = os.walk('F:/ELEC498modelskernels/')
#flag to skip first entry since walk is not subscriptable
flag = 0
#list which will hold all the filenames to construct legend for final graph
legendvals = []
#iterate over parts of the walk
for root, dirs, files in walked:
    if flag == 0:
        flag = 1
        continue
    for filename in files:
        if filename == '2-conv-2048-nodes-3-dense-3-kernelsize-elu-activation-0.1-dropoutrate-0.01-learningrate-timestamp-1553721359.pkl':
            os.chdir(root)
            with open(filename,'rb') as f:
                data = pickle.load(f)
                for key in data.keys():
                    print(key)
                val_acc = data['val_acc']
                xvals = range(len(val_acc))
                sns.set_style("darkgrid")
                sns.set_palette(sns.xkcd_palette(colors))
                plt.plot(val_acc)
                legendvals.append(filename)
                plt.title('Accuracy per Epoch for the Best Model', fontsize = 25)
                plt.xlabel("Epoch", fontsize = 20)
                plt.ylabel("Accuracy", fontsize = 20)
                plt.xlim(0, 40)

            

                
plt.legend(legendvals, prop = {'size': 14})
plt.show()
                
        