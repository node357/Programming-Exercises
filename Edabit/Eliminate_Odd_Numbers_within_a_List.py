###################################################################
#
# Eliminate Odd Numbers within a List
######################################
#
# Create a function that returns all values in a list that aren't' odd.
#
# Rules
########
# Return all valid numbers (even) in the order they were given.
###################################################################

def noOdds(lst):
        return [i for i in lst if i % 2 == 0]


