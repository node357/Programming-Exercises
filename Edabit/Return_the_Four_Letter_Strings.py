#############################################################################
#
# Return the Four Letter Strings 
##################
#
# Create a function that takes a list of strings. Return all words in the list
# that are exactly four letters.
#
#############################################################################

def isFourLetters(lst):
      return [i for i in lst if len(i) == 4]

