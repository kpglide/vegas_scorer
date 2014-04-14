import unittest

from OOP_Prototype import Course, Player

class Course_TDD(unittest.TestCase):

	# USGA min course slope == 55
	def test_return_error_message_if_slope_below_USGA_min(self):
		self.assertRaises(ValueError, Course, 'Rivermont', 54)

	# USGA max course slope == 155
	def test_return_error_message_if_slope_above_USGA_max(self):
		self.assertRaises(ValueError, Course, 'Rivermont', 156)

class Player_TDD(unittest.TestCase):

	def setUp(self):
		self.player = Player('kevin', 'male', 17)

	def test_return_error_message_if_gender_is_num(self):
		self.assertRaises(ValueError, Player, 'kevin', 4, 17)

	# gender must be M/Male/m/male or F/Female/f/female
	def test_return_message_if_gender_is_wrong_string(self):
		self.assertRaises(ValueError, Player, 'kevin', 'cat', 17)

	# 36.4 is max USGA index for males
	def test_male_handicap_index_is_not_too_high(self):
		self.assertRaises(ValueError, Player, 'kev', 'm', 36.5)

	# 40.4 is max USGA index for femails
	def test_female_handicap_index_is_not_too_high(self):
		self.assertRaises(ValueError, Player, 'jill', 'female', 40.5)

	def test_handicap_index_is_number(self):
		self.assertRaises(ValueError, Player, 'jill', 'female', 'cat')

	def test_course_handicap_calculation(self):
		self.player.calculate_course_handicap(131)
		self.assertEqual(20, self.player.course_handicap)