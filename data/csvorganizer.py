import csv
filenames = []
baseyear = 2007

#create a list of all filenames based on template
for i in range(12):
	currentyear = baseyear + i
	filenames.append("eng-daily-0101" + str(currentyear) + "-1231" + str(currentyear) + " (" + str(0) + ").csv")
#remove the last 2 since they don't exist
print(filenames)	

		
#create new master csv

with open("master.csv", "wt", newline = "") as f:
	writer = csv.writer(f)
	#iterate through all files in the folder
	for file in filenames:
		with open(file, "rt") as k:
			reader = csv.reader(k)
			#write filename as first row always
			writer.writerow(file)
			#write rest of the file to the master
			for row in reader:
				writer.writerow(row)