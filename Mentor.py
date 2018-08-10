class Mentor:
	"""
	Class for Mentor
	Nothing else needed, all variables are public so that they can easily be used in the script
	"""
	
	def __init__(self, name, answers):
		self.name = name
		self.answers = answers
		self.student = None
		self.hasStudent = false
		self.matchScore = 0
		
		
