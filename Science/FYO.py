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

    return final

def longAnswers(fileName):
    with open(fileName, encoding = "UTF-8") as csvfile:
        reader = csv.DictReader(csvfile)
        hobbies, worries, language, final = [], [], [], []

        for line in reader:
                hobbies.append(line['hobbies'])
                worries.append(line['worries'])
                language.append(line['language'])

        for i in range(len(hobbies)):
            longAnswers = [hobbies[i], worries[i], language[i]]
            final.append(longAnswers)
    
    return final

def weight(q):
    weight = [2, 1.5, 0.75, 0.5]
    return weight[q]

def mentor(fileName):
    with open(fileName, encoding="UTF-8") as csvfile:
        reader = csv.DictReader(csvfile)
        name, mentor, email = [], [], ""
        mLA = longAnswers(mentorFileName)
        
        for line in reader:
            name.append(line['name'])
            email.append(line['email'])
        
        program, commute, helpme, interests = separate(mentorFileName, "program"), separate(mentorFileName, "commute"), separate(mentorFileName, "helpme"), separate(mentorFileName, "interests")

        for i in range(len(program)):
            answers = [program[i], commute[i], helpme[i].split(', '), interests[i].split(', ')]
            mentor.append(Mentor(name[i], answers, mLA[i], email[i]))
            answers = []

    return mentor

def student(fileName):
    with open(fileName, encoding="UTF-8") as csvfile:
        reader = csv.DictReader(csvfile)
        name, student, answers, email = [], [], [], []
        sLA = longAnswers(studentFileName)
        
        for line in reader:
            name.append(line['name'])
            email.append(line['email'])
        
        program, commute, helpme, interests = separate(studentFileName, "program"), separate(studentFileName, "commute"), separate(studentFileName, "helpme"), separate(studentFileName, "interests")

        for i in range(len(program)):
            answers = [program[i], commute[i], helpme[i], interests[i]]
            student.append(Student(name[i], answers, sLA[i], email[i]))
            answers = []

    return student

mentorList = mentor(mentorFileName)
studentList = student(studentFileName)

for i in range(len(studentList)):
    stud = studentList[i]
    for j in range(len(mentorList)):
        mentor = mentorList[j]
        stud.matches[mentor.getName()] = 0
        for k in range(len(stud.getAnswers())):
            answers = stud.getAnswers()[k]
            if type(answers) == list:
                for answer in answers:
                    if answer in mentor.getAnswers()[k]:
                        stud.matches[mentor.getName()] += weight(k)
            elif answers == mentor.getAnswers()[k]:
                stud.matches[mentor.getName()] += weight(k)

for student in studentList:
    for mentor in mentorList:
        for k in range(len(student.getLongAnswers())):
            if student.getLongAnswers()[k] and mentor.getLongAnswers()[k]:
                sim = student.getLongAnswers()[k].similarity(mentor.getLongAnswers()[k])
                student.matches[mentor.getName()] += 0.75 * sim

for student in studentList:
    for mentor in mentorList:
        for mentorKey in student.getBestToWorse():
            if mentor.name == mentorKey[0]:
                student.topMentors.append(mentor)

for i in range(len(mentorList)):
    for student in studentList:
        if not student.isMatched:
            potTopMentor = student.topMentors.pop(0)
            if not potTopMentor.hasStudent:
                potTopMentor.match(student)
                student.isMatched = True
            else:
                if student.matches[potTopMentor.name] > potTopMentor.student.matches[potTopMentor.name]:
                    potTopMentor.student.isMatched = False
                    potTopMentor.unmatch()
                    potTopMentor.match(student)
                    student.isMatched = True

unmatchedStudents = []     
for student in studentList:
    if not student.isMatched:
        unmatchedStudents.append(student)
        for mentor in mentorList:
            for mentorKey in student.getBestToWorse():
                if mentor.name == mentorKey[0]:
                    student.topMentors.append(mentor)

while unmatchedStudents:
    for i in range(len(mentorList)):
        for student in unmatchedStudents:
            potTopMentor = student.topMentors.pop(0)
            if not potTopMentor.hasStudent2:
                potTopMentor.match2(student)
                student.isMatched = True
            else:
                if student.matches[potTopMentor.name] > potTopMentor.student.matches[potTopMentor.name]:
                    potTopMentor.student.isMatched = False
                    potTopMentor.unmatch2()
                    potTopMentor.match2(student)
                    student.isMatched = True

            if student.isMatched:
                unmatchedStudents.remove(student)

with open('C:/Users/socce/Desktop/Business1Matches.csv', mode='w', encoding='utf-8') as mentor_file:
    mentor_writer = csv.writer(mentor_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    mentor_writer.writerow(["mentee", "mentor(s)"])
    for i, mentor in enumerate(mentorList):
        if mentor.hasStudent2:
            mentor_writer.writerow([mentor.name.strip() + ": {}".format(mentor.email.strip()),
            mentor.student.name.strip() + ": {}".format(mentor.student.email.strip()) + "+" + mentor.student2.name.strip() + ": {}".format(mentor.student2.email.strip())])
        else:
            mentor_writer.writerow([mentor.name.strip() + ": {}".format(mentor.email.strip()), mentor.student.name.strip() + ": {}".format(mentor.student.email.strip())])
