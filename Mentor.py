class Mentor:
	"""
	Class for Mentor
	Nothing else needed, all variables are public so that they can easily be used in the script
	"""
	
	def __init__(self, name, answers):
		self.name = name
		self.answers = answers
		self.student = None
		self.hasStudent = False
		self.matchScore = 0
		self.secondStudent = None
		self.hasSecondStudent = False
		
	def unmatch(self):
		tempStudent = self.student
		tempStudent.isMatched = False
		tempStudent.mentor = None
		self.student = None
		self.hasStudent = False
		
	def match(self, student):
		self.student = student
                self.hasStudent = True
                self.matchScore = student.matches(self.name)
                student.mentor = self
                student.isMatched = True
