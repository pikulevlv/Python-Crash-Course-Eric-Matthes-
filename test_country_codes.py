import unittest
from country_codes import get_country_code

class TestCountryCodes(unittest.TestCase):
	"""Tests for function get_country_code"""

	def test_country_codes(self):
		answer = get_country_code('Australia')
		self.assertEqual(answer, 'au')
	def test_country_not_codes(self):
		answer = get_country_code('Vietnam')
		self.assertEqual(answer, None)
		
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
