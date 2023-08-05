
# import unittest



# class TestTimes(unittest.TestCase):

# 	workweek = [Day(DaysEnum.MONDAY), Day(DaysEnum.TUESDAY), Day(DaysEnum.WEDNESDAY), Day(DaysEnum.THURSDAY), Day(DaysEnum.FRIDAY)]

# 	weekend = [Day(DaysEnum.SATURDAY), Day(DaysEnum.SUNDAY)]

# 	fullweek = workweek.copy()
# 	fullweek.extend(weekend)

# 	def test_expand_day_range(self):
# 		self.assertEqual(
# 			list(Days(DaysEnum.MONDAY, DaysEnum.FRIDAY)),
# 			self.workweek
# 		)

	
# 	def test_allweek_shortcuts(self):
# 		# TODO: implement assumption of pm if end time <= start time
# 		input_strings = [
# 			"All Week",
# 			"7 days a week",
# 			"7 days",
# 			"Every Day",
# 			"",# no date present, just a time -> assume all week
# 			"daily",
# 		]
# 		expected_result = self.fullweek
# 		self.run_tests(input_strings, expected_result)

# 	def test_create_from_none(self):
# 		with self.assertRaises(TypeError):
# 			Days.from_shortcut_string(None)
# 		with self.assertRaises(TypeError):
# 			Days(None, None)

# 	def test_create_from_unknown(self):
# 		with self.assertRaises(ValueError):
# 			Days.from_shortcut_string("cheeseburger")

# 	def test_workweek(self):
# 		input_strings = [
# 			"Weekdays",
# 			"5 days a week",
# 			"5 days",
# 			"Business Days",
# 			"workdays"
# 		]
# 		expected_result = self.workweek
# 		self.run_tests(input_strings,expected_result)

# 	def test_weekend(self):
# 		# TODO: implement assumption of pm if end time <= start time
# 		input_strings = [
# 			"Weekend",
# 			"Weekends",
# 		]
# 		expected_result = self.weekend
# 		self.run_tests(input_strings,expected_result)

# 	def test_equals(self):
# 		workweek = Days(DaysEnum.MONDAY, DaysEnum.FRIDAY)
# 		with self.assertRaises(NotImplementedError):
# 			workweek == "something else"
		
# 		self.assertEqual(workweek, workweek)


# 	def run_tests(self, input_strings, expected_result, **kwargs):
# 		for input_str in input_strings:
# 			print("Testing String: '", input_str)
# 			self.assertEqual(list(Days.from_shortcut_string(input_str, **kwargs)), expected_result)

# if __name__ == '__main__':
# 	unittest.main()