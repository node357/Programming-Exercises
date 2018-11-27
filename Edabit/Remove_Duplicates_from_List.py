#####################################################################################
#
# Remove Duplicates from List 
##################
#
# Create a function that takes a list of items, removes all duplicate items and
# returns a new list in the same sequential order as the old list (minus duplicates).
#
####################################################################################

def removeDups(lst):
  result = []
  for i in lst:
    if i not in result:
      result.append(i)
  return result


