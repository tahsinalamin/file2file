'''
A program that takes input a CSV file (i,j,v) and generate a TXT file (i,j)

Author: Sikder Tahsin Al-Amin
Update: 16/4/18 - takes a csv file, stores the values in list and write into txt file

'''
import sys
import pandas as pd
import string
import csv

file_name='tree1000000.csv'

i=[]  #the i column
j=[]  #the j column


##open the CSV file and store them ###
with open(file_name) as csvDataFile:
    csvReader = csv.reader(csvDataFile,delimiter=',')
    for row in csvReader:
        int(row[0].replace(',', ''))
        i.append(int(row[0]))
        all_vertices.append(int(row[0]))
        int(row[1].replace(',', ''))
        j.append(int(row[1]))
        all_vertices.append(int(row[1]))


csvDataFile.close()
#print(len(i))
#print(len(j))

file_name=file_name.replace(".csv","")
print("CSV file: ",file_name)
write_file_name=file_name+".txt"
print("Text file: ",write_file_name)
file=open(write_file_name,"w")


for index in range(0,len(i)-1):
    row=str(i[index])+" "+str(j[index])
    file.write(row)
    #file.write(" ")
    #file.write(j[index])
    file.write('\n')

file.close()




