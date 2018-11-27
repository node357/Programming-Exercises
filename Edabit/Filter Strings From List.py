#############################################################################
#
# Filter Strings From List 
##################
#
# Create a function that takes a list of non-negative numbers and strings and
# returns a new list without the strings.
#
#############################################################################

def filter_list(lst):
        return [l for l in lst if isinstance(l, int)]
