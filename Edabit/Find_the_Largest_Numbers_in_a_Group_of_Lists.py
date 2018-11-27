###################################################################
#
# Find the Largest Numbers in a Group of Lists 
##################
#
# Create a function that takes a list of lists with integers or floats. Return
# a new (single) list with the largest numbers from each.
#
###################################################################

def findLargestNums(num_list):
  return [max(i) for i in num_list]

