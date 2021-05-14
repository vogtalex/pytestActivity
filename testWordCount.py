import unittest
import wordCount

class testCaseAdd(unittest.TestCase):
	def test_add(self):
		self.assertEqual(wordCount.wordCounter("This is 4 words."), 4)
		self.assertEqual(wordCount.wordCounter("A few more cool words."), 5)
		
	def test_add_numbers(self):
		self.assertEqual(wordCount.wordCounter("1 2 3 4 5 6 7 8"), 8)

	def test_add_spaces(self):
		self.assertEqual(wordCount.wordCounter(" This is incorrect"), 3)

if __name__ == '__main__':
	unittest.main()