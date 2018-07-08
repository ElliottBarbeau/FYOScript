import csv

def readcsv(uOttawa League of Legends):
    xfile = open(filename, "rU")
    reader = csv.reader(file, delimiter = ";")

    for row in reader:
        rowCount+= 1
    
    a = [[] for i in range(rowCount)]

    rowCount = 0
    for row in reader:
        a[rowCount].append(row)
        rowCount+=1

    xfile.close()
    return(a)

