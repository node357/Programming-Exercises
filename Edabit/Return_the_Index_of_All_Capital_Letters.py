###################################################################
#
# Return the Index of All Capital Letters 
##################
#
# Create a function that takes a single string as argument and returns an
# ordered list containing the indexes of all capital letters in the string.
#
###################################################################

def indexOfCaps(word):
  result = []
  for val in enumerate(word):
    if val[1].isupper():
      result.append(val[0])
  return result


