class Course(object):
	"""This is a class for creating golf courses."""
	
	def __init__(self, course_name, course_slope):
		"""This creates a course with a name and USGA slope rating."""	
		
		# Return an error message if the entered slope rating
		# is outside USGA limits.
		if course_slope < 55 or course_slope > 155:
			raise ValueError('Slope must be between 55 and 155 (inclusive)')
		
		self.name = course_name
		self.slope = course_slope


class Player(object):
	"""This is a class for creating golfers."""

	def __init__(self, player_name, gender, handicap_index):
		"""This creates a golfer with a name, gender and
		USGA handicap index.
		"""

		# Return an error if the gender is not 'male' or 'female'.
		gender_list = ['male', 'm', 'f', 'female']
		if str(gender).lower() not in gender_list:
			raise ValueError("Please enter 'male' or 'female' for gender.")
		
		# Return an error if the handicap index exceeds the USGA max, and
		# return an error if it's not a number.
		if (gender == 'm' or gender == 'male') and handicap_index > 36.4:
			raise ValueError("Male max index is 36.4")
		elif (gender == 'f' or gender == 'female') and handicap_index > 40.4:
			raise ValueError("Female max index is 40.4")
		elif (type(handicap_index) != int and type(handicap_index) != float):
			raise ValueError('Handicap index must be a number.')

		self.name = player_name
		self.gender = gender
		self.handicap_index = handicap_index
	
	def calculate_course_handicap(self, course_slope):
		"""This calculate the player's course handicap.
		It uses the USGA's formula from the following link.
		http://www.usga.org/handicapfaq/handicap_answer.asp?FAQidx=4
		"""

		course_handicap = int(round(self.handicap_index * course_slope
									/ 113.0))
		self.course_handicap = course_handicap	

	def calculate_hole_net_score(self, hole_difficulty, gross_score):
		"""This accepts the hole difficulty and player's
		gross score and parameters and returns the player's
		net score.
		"""

		# Calculate the number of 'strokes' the player receives.
		if self.course_handicap > 18:
			double_stroke_holes = self.course_handicap - 18
			if double_stroke_holes >= hole_difficulty:
				strokes = 2
			else: strokes = 1
		elif self.course_handicap >= hole_difficulty:
			strokes = 1
		else: strokes = 0
		strokes = strokes

		# The net score is gross score less 'strokes'.
		self.hole_net_score = gross_score - strokes


class Team(object):
	"""This is a class for creating two person golf teams."""

	def __init__(self, player1, player2):
		"""This assigns two players to a team."""

		self.team_name = player1.name + " & " + player2.name
		self.players = [player1, player2]
		self.team_overall_score = 0

	def calculate_team_hole_score(self):
		"""This calculates the team's 'Vegas' score.  To 
		create the score, the players' individual scores are
		combined together, with the lowest score placed first.
		E.g., if two players score 4 and 3, the team score is 34.
		See # See http://golf.about.com/od/golfterms/g/bldef_lasvegas.htm.
		"""

		scores = []
		for player in self.players:
			scores.append(player.hole_net_score)
		scores.sort()
		
		str_score = ''
		for score in scores:
			str_score += str(score)
		self.hole_score = int(str_score)	


class Match(object):
	"""This is a class for creating 'Vegas' golf matches."""
 
	def __init__(self, team1, team2, course):
		"""This scores a match of the 'Vegas' golf game.
		See http://golf.about.com/od/golfterms/g/bldef_lasvegas.htm
		"""

		self.teams = [team1, team2]
		self.course = course
		
		for team in self.teams:
			for player in team.players:
				player.calculate_course_handicap(self.course.slope) 
	
	def hole_points(self, score1, score2):
		"""This calculates the number points a team scored 
		on a hole of the 'Vegas' golf game."""

		points = max(score1, score2) - min(score1, score2)
		return points

	def play_hole(self, hole_difficulty):
		"""This plays of hole within a 'Vegas' golf
		match.
		"""

		for team in self.teams:
			for player in team.players:
				gross_score = input("Enter " + player.name + "'s score: ")
				player.calculate_hole_net_score(hole_difficulty, gross_score)
			team.calculate_team_hole_score()

		if self.teams[0].hole_score < self.teams[1].hole_score:
			self.teams[0].team_overall_score += self.hole_points(
					self.teams[0].hole_score, 
					self.teams[1].hole_score)
		elif self.teams[0].hole_score > self.teams[1].hole_score:
			self.teams[1].team_overall_score += self.hole_points(
					self.teams[0].hole_score, 
					self.teams[1].hole_score)

		print "{0} scored {1} on this hole.".format(self.teams[0].team_name,
													self.teams[0].hole_score)
		print "{0} scored {1} on this hole.".format(self.teams[1].team_name,
													self.teams[1].hole_score) 
		print "{0} have {1} total points.".format(
				self.teams[0].team_name,
				self.teams[0].team_overall_score)
		print "{0} have {1} total points.".format(
				self.teams[1].team_name,
				self.teams[1].team_overall_score)


# This is a test two hole match intended to confirm that the initial
# version of this program works from the command line.
if __name__ == "__main__":
	course = Course('Rivermont', 131)
	player1, player2, player3, player4 = (
			Player('kevin', 'male', 17),
			Player('tone', 'male', 20), 
			Player('norton', 'male', 28), 
			Player('rhett', 'm', 14))
	team1, team2, = Team(player1, player2), Team(player3, player4)
	match = Match(team1, team2, course)
	match.play_hole(10)
	match.play_hole(18)