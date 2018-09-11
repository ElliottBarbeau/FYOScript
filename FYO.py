import csv
import spacy
from Student import Student
from Mentor import Mentor

mentorFileName = "C:/Users/Elliott/Desktop/MentorInfo.csv"
studentFileName = "C:/Users/Elliott/Desktop/StudentInfo.csv"
nlp = spacy.load('en')

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

def mentorLongAnswers(fileName):
    with open(fileName, encoding = "Latin-1") as csvfile:
        reader = csv.DictReader(csvfile)
        interests = []
        tvShows = []
        sports = []
        music = []
        final = []

        for line in reader:
                interests.append(line['interests'])
                tvShows.append(line['tvShows'])
                sports.append(line['sports'])
                music.append(line['music'])

        for i, interest in enumerate(interests):
            longAnswers = []
            longAnswers.append(interest)
            longAnswers.append(tvShows[i])
            longAnswers.append(sports[i])
            longAnswers.append(music[i])
            final.append(list(longAnswers))
    
    return final

def studentLongAnswers(fileName):
    with open(fileName, encoding = "Latin-1") as csvfile:
        reader = csv.DictReader(csvfile)
        interests = []
        tvShows = []
        sports = []
        music = []
        final = []

        for line in reader:
                interests.append(line['interests'])
                tvShows.append(line['tvShows'])
                sports.append(line['sports'])
                music.append(line['music'])

        for i, interest in enumerate(interests):
            longAnswers = []
            longAnswers.append(interest)
            longAnswers.append(tvShows[i])
            longAnswers.append(sports[i])
            longAnswers.append(music[i])
            final.append(list(longAnswers))
    
    return final

def weight(q):
    if q == 0:
        return 2
    elif q == 1:
        return 0.5
    elif q == 2:
        return 0.5
    elif q == 3:
        return 1.5
    elif q == 4:
        return 1

def mentor(fileName):
    with open(fileName, encoding="Latin-1") as csvfile:
        reader = csv.DictReader(csvfile)
        name = []
        mentor = []
        answers = []
        
        for line in reader:
            name.append(line['name'])
        
        stream = streamSep(mentorFileName)
        internship = internshipSep(mentorFileName)
        clubs = clubsSep(mentorFileName)
        skills = skillsSep(mentorFileName)
        profSkills = profSkillsSep(mentorFileName)

        for i in range(0, len(stream)):
            mLA = mentorLongAnswers(mentorFileName)
            answers.append(stream[i])
            answers.append(internship[i])
            answers.append(clubs[i])
            answers.append(skills[i])
            answers.append(profSkills[i])
            mentor.append(Mentor(name[i], answers, mLA[i]))
            answers = []

    return(mentor)

def student(fileName):
    with open(fileName, encoding="Latin-1") as csvfile:
        reader = csv.DictReader(csvfile)
        name = []
        student = []
        answers = []
        
        for line in reader:
            name.append(line['name'])
        
        stream = streamSep(studentFileName)
        internship = internshipSep(studentFileName)
        clubs = clubsSep(studentFileName)
        skills = skillsSep(studentFileName)
        profSkills = profSkillsSep(studentFileName)

        for i in range(0, len(stream)):
            sLA = studentLongAnswers(studentFileName)
            answers.append(stream[i])
            answers.append(internship[i])
            answers.append(clubs[i])
            answers.append(skills[i])
            answers.append(profSkills[i])
            student.append(Student(name[i], answers, sLA[i]))
            answers = []

    return(student)

mentorList = mentor(mentorFileName)
studentList = student(studentFileName)

for i, stud in enumerate(studentList):
    for j, mentor in enumerate(mentorList):
        stud.dictionary[mentor.getName()] = 0
        for k, answers in enumerate(stud.getAnswers()):
            if type(answers == list):
                for answer in answers:
                    if answer in mentorList[i].getAnswers()[k]:
                        stud.dictionary[mentor.getName()] += weight(k)
            elif answers == mentor.getAnswers()[k]:
                stud.dictionary[mentor.getName()] += weight(k)

for i, stud in enumerate(studentList):
    for j, mentor in enumerate(mentorList):
        for k, answers in enumerate(stud.getLongAnswers()):
            doc1 = nlp(answers)
            doc2 = nlp(mentor.getLongAnswers()[k])
            sim = doc1.similarity(doc2)
            stud.dictionary[mentor.getName()] += sim
       
'''
Weights must be assigned before
Student dictionaries and mentor dictionaries must already be made
Length variable for topMentors must be determined
for student in indStudentList:
    for mentor in indMentorList:
        student.matches[mentor.name] = 0

for student in indStudentList:
    for mentor in indMentorList:
        for i in range(answerlist.length):
            if student.answers[i] == mentor.answers[i]:
                student.matches[mentor.name] += correctWeight[i]
            else:
                student.matches[mentor.name] -= wrongWeight[i]

for student in indStudentList:
    student.topMentors = student.getBestToWorse()[:topMentors.lengthVariable]

for i in range(topMentors.lengthVariable):
    for student in indStudentList:
        if student.isMatched is False:
            potTopMentor = student.topMentors.pop(0)
            if potTopMentor.hasStudent is False:
                potTopMentor.match(student)
            else:
                if student.matches(potTopMentor.name) > potTopMentor.matchScore:
                    potTopMentor.unmatch()
                    potTopMentor.match(student)

unmatchedStudents = []     
for student in indStudentList:
    if student.isMatched is False:
        unmatchedStudents.append(student)
        student.topMentors = student.getBestToWorse()[:topMentors.lengthVariable]

for i in range(topMentors.lengthVariable):
    for student in unmatchedStudents:
        if student.isMatched is False:
            potTopMentor = student.topMentors.pop(0)
            if potTopMentor.hasStudent2 is False:
                potTopMentor.match2(student)
            else:
                if student.matches(potTopMentor.name) > potTopMentor.matchScore:
                    potTopMentor.unmatch2()
                    potTopMentor.match2(student)
'''