
import csv
import os
import h5py
import numpy as np
from numpy import array, hstack, vstack


#set working directory
os.chdir('C:/Users/rajes/OneDrive/Documents/ELEC498renew/ELEC-498-Capstone/data')

#set up all values so they can be altered easily
year = 2008
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
currmonth = 0
day = 1
hour = 0
#initialize filename
filename = str(year) + '-' + str(months[currmonth]) + '-' + str(day) + '-' + str(hour)
         

#read in the h5 file
f = h5py.File('thiccBOI.hdf5', 'r')
#example access of h5 file
#list(f['2008']['April']['1']['0']['2008-April-1-0'])

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
            yvals[key][keyt][str(i)] = 'N'

flag = 0

#read in the y values (rainfall vals)
with open ('Master_numpy_withnoNulls_FIXED.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    
    for row in reader:
        #skip the first row
        if flag == 0:
            flag = 1
            continue
        yvals[row[1]][months[int(row[2]) - 1]][row[3]] = int(row[5])




#this comment is here just cause

#initialize data in correct shape
temp = np.zeros((24,31,31,3))
#init final list to store arrays in
npfinalx = np.array([])
npfinaly = np.array([])
finalx = []
finaly = []

#iterate over years
for year in range(2008, 2017):
    #iterate over months
    for currmonth in range(len(months)):
        #iterate over days
        for day in range(1,28):
            for compass in range(4):
                temp = np.zeros((24,31,31,3))
                try:
                    #append to preliminary list
                    finaly.append(yvals[str(year)][months[currmonth]][str(day)])
                except:
                    print("rainfall data not found, skipping")
                    continue
                #iterate over hours
                for hour in range(24):
                    #set proper filename variable
                    filename = str(year) + '-' + str(months[currmonth]) + '-' + str(day) + '-' + str(hour) + '-' + str(compass)
                    #iterate over rows
                    for i in range(31):
                        #attempt to extract row of the image for the current hour
                        try:
                            temprow = list(f[str(year)][months[currmonth]][str(day)][str(hour) + '-' + str(compass)][filename][i])
                        except:
                            #if the hour cannot be found then break (skip this record)
                            print("hour " + str(hour) + " for " + filename +  " not found, skipping")
                            break
                        #iterate over columns
                        for k in range(31):
                            #access a single one of those pixels
                            temppixel = temprow[k]
                            #iterate over RGB
                            for z in range(3):
                                temp[hour][i][k][z] = temppixel[z]
                #add to preliminary list of x values
                finalx.append(temp)


#remove all the null values from the lists (all skipped records)
for i in reversed(range(len(finaly))):
    if finaly[i] == 'N':
        del finaly[i]
        del finalx[i]

#convert the lists into arrays for storage
npfinaly = np.asarray(finaly)
npfinalx = np.asarray(finalx)


#write data to file
h5f = h5py.File('cleandata.h5', 'w')
h5f.create_dataset('dataset_x', data = npfinalx)
h5f.create_dataset('dataset_y', data = npfinaly)
h5f.close()
