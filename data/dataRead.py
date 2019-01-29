
import csv
import os
import h5py
import numpy as np
from numpy import array, hstack, vstack



os.chdir('C:/Users/rajes/OneDrive/Documents/ELEC498 numba 2/ELEC-498-Capstone/data')

#set up all values so they can be altered easily

year = 2008
months = ['April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'January', 'February', 'March']
currmonth = 0
day = 1
hour = 0
filename = str(year) + '-' + str(months[currmonth]) + '-' + str(day) + '-' + str(hour)
         


f = h5py.File('images2008.hdf5', 'r')

#print(list(f['2008']['April']['1']['0']['2008-April-1-0']))

#initialize data in correct shape
temp = np.zeros((24,31,31,3))

final = []

#iterate over hours in a day to start populating zeros array

for currmonth in range(1):
    for day in range(1,5):
        temp = np.zeros((24,31,31,3))
        for hour in range(24):
            filename = str(year) + '-' + str(months[currmonth]) + '-' + str(day) + '-' + str(hour)
            #list of pixels for a row of the array
            for i in range(31):
                #list of 3 element arrays representing pixels for a row of the array [R,G,B]
                print(hour)
                try:
                    temprow = list(f[str(year)][months[currmonth]][str(day)][str(hour)][filename][i])
                except:
                    print("hour " + str(hour) + " not found, skipping")
                    break
                for k in range(31):
                    #access a single one of those pixels
                    temppixel = temprow[k]
                    for z in range(3):
                        temp[hour][i][k][z] = temppixel[z]
        final.append(temp)

print(final)