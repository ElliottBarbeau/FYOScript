class Student:
	"""Class for student"""
	def __init__ (self, name, answers, longAnswers, email):
		self.longAnswers = longAnswers
		self.matches = {}
		self.name = name
		self.answers = answers
		self.isMatched = False
		self.mentor = None
		self.temp = []
		self.topMentors = []
		self.email = email
	
	def setMatch(self, key, score):
		self.matches[key] = score
	
	def getBestToWorse(self):
		toRet = sorted(self.matches.items(), key = lambda x:x[1])[::-1]
		return toRet

	def getAnswers(self):
		return self.answers

	def getLongAnswers(self):
		return self.longAnswers