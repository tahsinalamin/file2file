import sys
import pandas as pd
import string
import csv

file_name='tree1000000.csv'

i=[]  #the i column
j=[]  #the j column
all_vertices=[]


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


file_name=file_name.replace(".csv","")
print("CSV file: ",file_name)
write_file_name=file_name+".gxl"
print("Text file: ",write_file_name)
file=open(write_file_name,"w")


write_gxl="<gxl>"
file.write(write_gxl)
file.write('\n')
write_gxl="<graph id=\"G\" edgemode=\"directed\">"
file.write(write_gxl)
file.write('\n')

all_vertices=list(set(all_vertices)) ##finding all individual vertices
for index in range(0,len(all_vertices)):
    node="<node id=\""+str(all_vertices[index])+"\" />"
    file.write(node)
    file.write('\n')
    
for index in range(0,len(i)):
    row="<edge id=\"e"+str(index+1)+"\" from=\""+ str(i[index])+"\" to=\""+str(j[index])+"\" />"
    file.write(row)
    file.write('\n')

write_gxl="</graph>"
file.write(write_gxl)
file.write('\n')
write_gxl="</gxl>"
file.write(write_gxl)

file.close()
