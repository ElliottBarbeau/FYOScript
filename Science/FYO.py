import csv
import spacy
from Student import Student
from Mentor import Mentor

'''

// NOTE //

Headers: Timestamp, name, email, phoneNumber, temp, level, stream, internship, clubs, skills, profSkills, commuting, interests, tvShows, sports, music
newHeader: Timestamp,email,name,temp,stream,internship,commuting,city,clubs,skills,profSkills,interests,tvShows,sports,music,ethnicity,temp3
Matching Prioritization for 2020 needs to be Location > Ethnicity > everything else

// TODO //

FIX NATURAL LANGUAGE PROCESSING FOR SEMANTIC SIMILARiTY SCORES
Change header in csv files to match what I need
Run the script and make changes to weighting of some categories as necessary

'''

studentFileName = "C:/Users/socce/Desktop/Mentors.csv"
mentorFileName = "C:/Users/socce/Desktop/Mentees.csv"
nlp = spacy.load("en_core_web_md")

def readcsv(fileName):
    with open(fileName, encoding="UTF-8") as csvfile:
        reader = csv.DictReader(csvfile)
        a = []
        next(reader)
        for line in reader:
            a.append(line)  
    return(a)

def separate(fileName, arg):
    with open(fileName, encoding="UTF-8") as csvfile:
        reader = csv.DictReader(csvfile)
        final, temp = [], []
        
        for line in reader:
            temp.append(line[arg])
        
        for i in temp:
            if ";" in i:
                final.append(i.split(";"))
            else:
                final.append(i)

    return(final)

def mentorLongAnswers(fileName):
    with open(fileName, encoding = "UTF-8") as csvfile:
        reader = csv.DictReader(csvfile)
        interests, tvShows, sports, music, final = [], [], [], [], []

        for line in reader:
                interests.append(line['interests'])
                tvShows.append(line['tvShows'])
                sports.append(line['sports'])
                music.append(line['music'])

        for i, interest in enumerate(interests):
            longAnswers = []
            longAnswers.extend((interest, tvShows[i], sports[i], music[i]))
            final.append(list(longAnswers))
    
    return final

def studentLongAnswers(fileName):
    with open(fileName, encoding = "UTF-8") as csvfile:
        reader = csv.DictReader(csvfile)
        interests, tvShows, sports, music, ethnicity, final = [], [], [], [], [], []

        for line in reader:
            interests.append(line['interests'])
            tvShows.append(line['tvShows'])
            sports.append(line['sports'])
            music.append(line['music'])
            ethnicity.append(line['ethnicity'])

        for i, interest in enumerate(interests):
            longAnswers = []
            longAnswers.extend((interest, tvShows[i], sports[i], music[i], ethnicity[i]))
            final.append(list(longAnswers))
    
    return final

def weight(q):
    weight = [2, 0.5, 0.5, 1.5, 1]
    return weight[q]

def mentor(fileName):
    with open(fileName, encoding="UTF-8") as csvfile:
        reader = csv.DictReader(csvfile)
        name, mentor, answers = [], [], []
        
        for line in reader:
            name.append(line['name'])
        
        stream, internship, clubs, skills, profSkills = separate(mentorFileName, "stream"), separate(mentorFileName, "internship"), separate(mentorFileName, "clubs"), separate(mentorFileName, "skills"), separate(mentorFileName, "profSkills")

        for i in range(0, len(stream)):
            mLA = mentorLongAnswers(mentorFileName)
            answers.extend((stream[i], internship[i], clubs[i], skills[i], profSkills[i]))
            mentor.append(Mentor(name[i], answers, mLA[i]))
            answers = []

    return(mentor)

def student(fileName):
    with open(fileName, encoding="UTF-8") as csvfile:
        reader = csv.DictReader(csvfile)
        name, student, answers = [], [], []
        
        for line in reader:
            name.append(line['name'])
        
        stream, internship, clubs, skills, profSkills = separate(studentFileName, "stream"), separate(studentFileName, "internship"), separate(studentFileName, "clubs"), separate(studentFileName, "skills"), separate(studentFileName, "profSkills")

        for i in range(0, len(stream)):
            sLA = studentLongAnswers(studentFileName)
            answers.extend((stream[i], internship[i], clubs[i], skills[i], profSkills[i]))
            student.append(Student(name[i], answers, sLA[i]))
            answers = []

    return(student)

mentorList = mentor(mentorFileName)
studentList = student(studentFileName)

for student in studentList:
    for answer in student.getLongAnswers():
        student.nlpAnswers.append(nlp(answer))

for mentor in mentorList:
    for answer in mentor.getLongAnswers():
        mentor.nlpAnswers.append(nlp(answer))

for i, stud in enumerate(studentList):
    for j, mentor in enumerate(mentorList):
        stud.matches[mentor.getName()] = 0
        for k, answers in enumerate(stud.getAnswers()):
            if type(answers == list):
                for answer in answers:
                    if answer in mentor.getAnswers()[k]:
                        stud.matches[mentor.getName()] += weight(k)
            elif answers == mentor.getAnswers()[k]:
                stud.matches[mentor.getName()] += weight(k)

for student in studentList:
    for mentor in mentorList:
        if student.getNlpAnswers()[0] is not "" and mentor.getNlpAnswers()[0] is not "":
            sim = student.getNlpAnswers()[0].similarity(mentor.getNlpAnswers()[0])
            student.matches[mentor.getName()] += 0.75 * sim

for student in studentList:
    student.temp = student.getBestToWorse()
    for mentor in mentorList:
        for mentorKey in student.temp:
            if mentor.name == mentorKey[0]:
                student.topMentors.append(mentor)

for i in range(len(mentorList)):
    for student in studentList:
        if not student.isMatched:
            potTopMentor = student.topMentors.pop(0)
            if not potTopMentor.hasStudent:
                potTopMentor.match(student)
            else:
                if student.matches[potTopMentor.name] > potTopMentor.student.matches[potTopMentor.name]:
                    potTopMentor.unmatch()
                    potTopMentor.match(student)

unmatchedStudents = []     
for student in studentList:
    if not student.isMatched:
        unmatchedStudents.append(student)
        student.temp = student.getBestToWorse()
        for mentor in mentorList:
            for mentorKey in student.temp:
                if mentor.name == mentorKey[0]:
                    student.topMentors.append(mentor)

for i in range(len(mentorList)):
    for student in unmatchedStudents:
        if not student.isMatched:
            potTopMentor = student.topMentors.pop(0)
            if not potTopMentor.hasStudent2:
                potTopMentor.match2(student)
            else:
                if student.matches[potTopMentor.name] > potTopMentor.student.matches[potTopMentor.name]:
                    potTopMentor.unmatch2()
                    potTopMentor.match2(student)

with open('C:/Users/socce/Desktop/Business1Matches.csv', mode='w', encoding='utf-8') as mentor_file:
    mentor_writer = csv.writer(mentor_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    mentor_writer.writerow(["mentee", "mentor(s)"])
    for i, mentor in enumerate(mentorList):
        if mentor.hasStudent2:
            mentor_writer.writerow([mentor.name.strip(), mentor.student.name.strip() + "+" + mentor.student2.name.strip()])
        else:
            mentor_writer.writerow([mentor.name.strip(), mentor.student.name.strip()])