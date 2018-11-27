#############################################################################
#
# Return the Middle Character(s) in a String 
##################
#
# Create a function that takes a string and returns the middle character(s). If
# the word's length is odd, return the middle character. If the word's length
# is even, return the middle two characters.
#
#############################################################################

def get_middle(word):
    if len(word) % 2 == 0:
        return word[len(word)/2-1:len(word)/2+1]
    else:
        return word[len(word)/2]

print get_middle('inhabitent')


