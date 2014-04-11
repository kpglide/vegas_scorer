#vegas.py

class Course(object):
	# create course using name and
	# USGA course slope
	def __init__(self, course_name, course_slope):
		self.name = course_name
		self.slope = course_slope

class Player(object):
	
	# create player using player name
	# and his/her USGA handicap index
	def __init__(self, player_name, handicap_index):
		self.name = player_name
		self.handicap_index = handicap_index
	
	# calculate player's course 
	# handicap using formula from the USGA
	# http://www.usga.org/handicapfaq/handicap_answer.asp?FAQidx=4
	def calculate_course_handicap(self, course_slope):
		course_handicap = int(round(self.handicap_index * course_slope
							/ 113.0))
		return course_handicap