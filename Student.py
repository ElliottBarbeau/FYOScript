class Student:
	"""Class for student"""
	
	def __init__ (self, name, answers):
		self.name = name
		self.answers = answers
		self.matches = {}
		self.isMatched = false
		self.mentor = None
		self.topMentors = []
	
	def setMatch(self, key, score):
		self.matches[key] = score
	
	def getBestToWorse(self):
		toRet = sorted(self.matches)
		toRet.reverse()
		return toRet
	
	
	
	
	
