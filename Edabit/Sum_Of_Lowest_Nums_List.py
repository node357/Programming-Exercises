#############################################################################
#
# Return the sum of the lowest numbers in the list
##################
#
# Create a function that takes the two lowest numbers in a list, and return the
# sum of them
#
#############################################################################

def sum_lowest(numbers):
    return sum([sorted(numbers)[0], sorted(numbers)[1]])
    
print(sum_lowest([1,3,2,5,6]))
