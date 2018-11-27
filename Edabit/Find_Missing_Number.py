###################################################################
#
# Find the Missing Number
##################
#
# Create a function that takes a list of numbers between 1 and 10 
# (excluding one number) and returns the missing number.
#
###################################################################

def missing_nums(lst):
      return [i for i in sorted(range(1, 10 + 1)) if not i in lst][0]

