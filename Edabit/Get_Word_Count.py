####################################################################
#
# Get Word Count
#
# Create a function that takes a string and returns the word count. 
# The string will be a sentence.
#
#
####################################################################

# Solution 1
def count_words(txt):
  return len([i for i in txt])

print count_words('thisisastring')

# Solution 2

def count_words(txt):
    return len([i != '' for i in txt])

print count_words('thisisastring')
