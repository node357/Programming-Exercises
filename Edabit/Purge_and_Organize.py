##################################################################################
#
# Purge and Organize 
##################
#
# Given a list of numbers, write a function that returns a list that...
#
# 1) Has all duplicate elements removed. 
# 2) Is sorted from least value to greatest value.
#
##################################################################################

def unique_sort(lst):
      return sorted([i for i in set(lst)])
