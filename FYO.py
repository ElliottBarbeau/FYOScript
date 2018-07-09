import csv

def readcsv(fileName):
    rowCount = 0
    with open(fileName, encoding="Latin-1") as csvfile:
        reader = csv.reader(csvfile)
        a = []
        lineCount = 0
        next(reader)
        
        for line in reader:
            a.append(line)
            lineCount=+1            
    return(a)

print(readcsv("C:/Users/Owner/Desktop/FYO.csv"))