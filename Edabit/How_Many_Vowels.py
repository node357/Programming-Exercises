#############################################################################
#
# How Many Vowels 
##################
#
# Create a function that takes a string and returns the number (count) of
# vowels contained within it.
#
# Rules
########
# a, e, i, o, u are considered vowles (not y).
# Return an integer.
#############################################################################

def count_vowels(txt):
	vowles = ['a','e','i','o','u']
	cnt = 0
	for i in txt.lower():
		if i in vowles:
			cnt += 1
	return cnt

print count_vowels('Nightmare')
# More Pythonic Way

def count_vowels(txt):
	return sum([1 for num in txt.lower() if num in ['a','e','i','o','u']])

print count_vowels('Nightmare')


