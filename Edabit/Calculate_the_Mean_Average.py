#############################################################################
#
# Calculate the Mean Average 
##################
#
# Create a function that takes a list of numbers and returns the mean average
# (round to two decimal places).
#
#############################################################################

def mean(lst):
  result = float(sum(lst)) / max(len(lst), 1)
  return float(str('%.2f' % result))

# A more simplistic approach 

def mean(lst):
  return round(sum(lst) / len(lst), 2)

