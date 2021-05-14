import palindrome

def test_answer():
	assert palindrome.palindromeChecker("racecar") == True
	assert palindrome.palindromeChecker("parrot") == False

def test_numbers():
	assert palindrome.palindromeChecker("123454321") == True

def test_spaces():
	assert palindrome.palindromeChecker("dog god") == True
