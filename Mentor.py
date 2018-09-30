class Mentor:

    def __init__(self, name, answers, longAnswers):
        self.longAnswers = longAnswers
        self.name = name
        self.answers = answers
        self.student = None
        self.hasStudent = False
        self.matchScore = 0
        self.student2 = None
        self.hasStudent2 = False
        self.matchScore2 = 0

    def unmatch(self):
        tempStudent = self.student
        tempStudent.isMatched = False
        tempStudent.mentor = None
        self.student = None
        self.hasStudent = False

    def match(self, student):
        self.student = student
        self.hasStudent = True
        self.matchScore = student.matches[self.name]
        student.mentor = self
        student.isMatched = True

    def match2(self, student):
        self.student2 = student
        self.hasStudent2 = True
        self.matchScore2 = student.matches[self.name]
        student.mentor = self
        student.isMatched = True

    def unmatch2(self):
        tempStudent = self.student2
        tempStudent.isMatched = False
        tempStudent.mentor = None
        self.student2 = None
        self.hasStudent2 = False

    def getAnswers(self):
        return self.answers

    def getName(self):
        return self.name

    def getLongAnswers(self):
        return self.longAnswers
        