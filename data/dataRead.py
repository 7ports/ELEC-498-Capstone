
import csv
import os
import h5py
import numpy as np
from numpy import array, hstack, vstack



os.chdir('C:/Users/rajes/OneDrive/Documents/ELEC498 numba 2/ELEC-498-Capstone/data')

#set up all values so they can be altered easily
year = 2008
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
currmonth = 0
day = 1
hour = 0
filename = str(year) + '-' + str(months[currmonth]) + '-' + str(day) + '-' + str(hour)
         


f = h5py.File('images2008.hdf5', 'r')
#example access of h5 file
#print(list(f['2008']['April']['1']['0']['2008-April-1-0']))

yvals = {}


#keys for the dictionary go year, month, day
for i in range(2008,2018):
    yvals[str(i)] = {}
for i in range(12):
    for key in yvals.keys():
        yvals[key][months[i]] = {}
for i in range(1,28):
    for key in yvals.keys():
        for keyt in yvals[key].keys():
            yvals[key][keyt][str(i)] = 0

flag = 0

with open ('Master_numpy_withNULLS.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    
    for row in reader:
        #skip the first row
        if flag == 0:
            flag = 1
            continue
        #skip null values
        if row[5] == 'Null':
            continue
        yvals[row[1]][months[int(row[2]) - 1]][row[3]] = int(row[5])


print(yvals)


#initialize data in correct shape
temp = np.zeros((24,31,31,3))
#init final list to store arrays in
finalx = []
finaly = []

#iterate over years
for year in range(2008, 2017):
    #iterate over months
    for currmonth in range(len(months)):
        #iterate over days
        for day in range(1,28):
            temp = np.zeros((24,31,31,3))
            try:
                finaly.append(yvals[str(year)][months[currmonth]][str(day)])
            except:
                print("rainfall data not found, skipping")
                continue
            #iterate over hours
            for hour in range(24):
                #set proper filename variable
                filename = str(year) + '-' + str(months[currmonth]) + '-' + str(day) + '-' + str(hour)
                #iterate over rows
                for i in range(31):
                    #attempt to extract row of the image for the current hour
                    try:
                        temprow = list(f[str(year)][months[currmonth]][str(day)][str(hour)][filename][i])
                    except:
                        #if the hour cannot be found then break
                        print("hour " + str(hour) + " for " + filename +  " not found, skipping")
                        break
                    #iterate over columns
                    for k in range(31):
                        #access a single one of those pixels
                        temppixel = temprow[k]
                        #iterate over RGB
                        for z in range(3):
                            temp[hour][i][k][z] = temppixel[z]
            #add to the final array
            #access y value from dictionary
            finalx.append(temp)
            

print(finaly)
