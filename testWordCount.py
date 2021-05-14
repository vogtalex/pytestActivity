import unittest
import wordCount

class testCaseAdd(unittest.TestCase):
	def test_add(self):
		self.assertEqual(wordCount.wordCounter("This is 4 words."), 4)
		self.assertEqual(wordCount.wordCounter("A few more cool words."), 5)


if __name__ == '__main__':
	unittest.main()