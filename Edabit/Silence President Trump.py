#############################################################################
#
# Silence President Trump! 
##################
#
# Congratulations, you're the new CTO of Twitter. You've received direct orders
# from Jack Dorsey to silence Donald Trump, but not by deleting his account.
# How is that possible? By removing every vowel from his tweets, essentially
# neutering him.
#
# Rules
########
# Create a function that takes a string as an argument. 
# Return a new string with all vowels removed.
#############################################################################

def silence_Trump(txt):
  return ''.join([x for x in txt if not x in ['a','e','i','o','u','A','E','I','O','U']])
