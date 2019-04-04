import os
import h5py


os.chdir('C:/Users/rajes/OneDrive/Documents/ELEC498renew/ELEC-498-Capstone/data')


#print(list(f['2008']['April']['1']['0']['2008-April-1-0-0']))
f = h5py.File('thiccBOI.hdf5', 'r')
print(list(f['2008']['April']['1']))
