#############################################################################
#
# Return a List of Sublists 
##################
#
# Create a function that returns a list containing sublists, each of a certain
# number of items, all set to either a string or an integer.
#
#############################################################################

def matrix(x, y, z):
	"""Return a x by y matrix containing z values"""
    row, column = x, y
    return [[z for i in range(column)] for i in range(row)]
    

