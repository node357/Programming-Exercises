#############################################################################
#
# Find the Smallest and Biggest Numbers
##################
#
# Create a function that accepts a list of numbers and return both the minimum
# and maximum numbers, in that order (as a list).
#
#############################################################################

def minMax(nums):
  i = sorted(nums)[0]
  j = sorted(nums)[-1]
  return [i, j]

# More Pythonic Way

def minMax(nums):
    return [min(nums), max(nums)]



