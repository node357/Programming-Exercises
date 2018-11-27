###################################################################
#
# X's and O's 
##############
#
# Create a function that takes a string, checks if it has the 
# same number of 'x's and 'o's and returns either True or False.
#
###################################################################

def XO(text):
    return text.lower().count('x') == text.lower().count('o')

