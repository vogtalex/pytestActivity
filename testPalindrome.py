import unittest
import palindrome

class testCaseAdd(unittest.TestCase):
	def test_add(self):
		self.assertEqual(palindrome.palindromeChecker("racecar"), True)
		self.assertEqual(palindrome.palindromeChecker("Parrot"), False)

	def test_add_numbers(self):
		self.assertEqual(palindrome.palindromeChecker("123454321"), True)

	def test_add_spaces(self):
		self.assertEqual(palindrome.palindromeChecker("dog god"), True)


if __name__ == '__main__':
	unittest.main()