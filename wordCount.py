def wordCounter(string):
	x = 1
	i = 0
	while i < len(string):
		if(string[i] == ' '):
			x = x + 1
		i = i + 1
	return x

print('\nThis program will determine the number of words in a sentence.')
