###################################################################
#
# Find the Minimum, Maximum, Length and Average Values
##################
#
# Create a function that takes List of numbers and returns the following statistics:
#
#  1) Minimum Value
#  2) Maximum Value
#  3) Sequence Length
#  4) Average Value
#
###################################################################

def minMaxLengthAverage(arr):
	return [min(arr), max(arr), len(arr), float(sum(arr) / max(len(arr), 1))]


