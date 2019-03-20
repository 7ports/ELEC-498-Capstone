import pickle
import os
import matplotlib.pyplot as plt
import seaborn as sns



os.chdir('C:/Users/rajes/OneDrive/Documents/ELEC498renew/ELEC-498-Capstone/data')
#preform walk and save in a variable
walked = os.walk('C:/Users/rajes/OneDrive/Documents/ELEC498renew/ELEC-498-Capstone/data/models')
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
        if filename[-4:] == '.pkl':
            os.chdir(root)
            with open(filename,'rb') as f:
                data = pickle.load(f)
                val_acc = data['val_acc']
                xvals = range(len(val_acc))
                sns.set_style("darkgrid")
                plt.plot(val_acc)
                legendvals.append(filename)
                plt.title('Accracy per Epoch')
plt.legend(legendvals)
plt.show()
                
        