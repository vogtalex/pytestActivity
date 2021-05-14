import wordCount

def test_answer():
	assert wordCount.wordCounter("This is 4 words.") == 4
	assert wordCount.wordCounter("A few more cool words.") == 5

def test_numbers():
	assert wordCount.wordCounter("1 2 3 4 5 6 7 8") == 8
	
def test_spaces():
	assert wordCount.wordCounter(" This is incorrect") == 3