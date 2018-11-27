#############################################################################
#
# Compare Strings by Sum of Characters
##########################################
#
# Create a function that takes two strings as arguments and return either
# True or False depending on whether the number of their charcters
# is equal or not.
#
#############################################################################

def comp(txt1, txt2):
	try:
		return True if len(txt1) == len(txt2) or len(txt2) == len(txt1) else False
	except ValueError as err:
		return err
