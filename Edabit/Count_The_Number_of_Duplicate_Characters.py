#############################################################################
#
# Count The Number of Duplicate Characters 
##################
#
# Create a function that takes a string and returns the number of alphanumeric
# characters that occur more than once.
#
# Notes
########
# The input string can be assumed to contain only alphanumeric characters 
# (digits + uppercase and lowercase letters).
#############################################################################

def duplicate_count(txt):
    return sum([1 for i in set(txt.lower()) if txt.count(i) > 1])


