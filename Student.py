class Student:
	"""Class for student"""
	
	def __init__ (self, name, answers):
		self.name = name
		self.answers = answers
		self.matches = {}
		self.isMatched = False
		self.mentor = None
		self.topMentors = []
	
	def setMatch(self, key, score):
		self.matches[key] = score
	
	def getBestToWorse(self):
		toRet = sorted(self.matches.items(), key = lambda x:x[1])
		toRet.reverse()
		return toRet
	
	
	
	
	
