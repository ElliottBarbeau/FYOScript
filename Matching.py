"""
Weights must be assigned before
Student dictionaries and mentor dictionaries must already be made
Length variable for topMentors must be determined

"""

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

##if there are still unmatched, keep incrementing lengthvariable and repeat last for lop
