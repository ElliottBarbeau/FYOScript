import csv

def readcsv(fileName):
    with open(fileName, encoding="Latin-1") as csvfile:
        reader = csv.DictReader(csvfile)
        a = []
        next(reader)
        
        for line in reader:
            a.append(line)         
    return(a)

def streamSep(fileName):
    with open(fileName, encoding="Latin-1") as csvfile:
        reader = csv.DictReader(csvfile)
        final = []
        temp = []
        
        for line in reader:
            temp.append(line['stream'])
        
        for i in temp:
            if ";" in i:
                final.append(i.split(";"))
            else:
                final.append(i)

    return(final)

def internshipSep(fileName):
    with open(fileName, encoding="Latin-1") as csvfile:
        reader = csv.DictReader(csvfile)
        final = []
        temp = []
        
        for line in reader:
            temp.append(line['internship'])
        
        for i in temp:
            if ";" in i:
                final.append(i.split(";"))
            else:
                final.append(i)

    return(final)

def clubsSep(fileName):
    with open(fileName, encoding="Latin-1") as csvfile:
        reader = csv.DictReader(csvfile)
        final = []
        temp = []
        
        for line in reader:
            temp.append(line['clubs'])
        
        for i in temp:
            if ";" in i:
                final.append(i.split(";"))
            else:
                final.append(i)

    return(final)

def skillsSep(fileName):
    with open(fileName, encoding="Latin-1") as csvfile:
        reader = csv.DictReader(csvfile)
        final = []
        temp = []
        
        for line in reader:
            temp.append(line['skills'])
        
        for i in temp:
            if ";" in i:
                final.append(i.split(";"))
            else:
                final.append(i)

    return(final)

def profSkillsSep(fileName):
    with open(fileName, encoding="Latin-1") as csvfile:
        reader = csv.DictReader(csvfile)
        final = []
        temp = []
        
        for line in reader:
            temp.append(line['profSkills'])
        
        for i in temp:
            if ";" in i:
                final.append(i.split(";"))
            else:
                final.append(i)

    return(final)

print(streamSep("C:/Users/Owner/Desktop/FYO.csv"))