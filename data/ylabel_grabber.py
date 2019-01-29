
import csv 
import os

os.chdir('C:/Users/rajes/OneDrive/Documents/ELEC498 numba 2/ELEC-498-Capstone/data')


with open("Master_numpy_withNulls.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    data = []
    for row in readCSV:
        data.append(row[:7])

for x in data:
    print(x[0])
    