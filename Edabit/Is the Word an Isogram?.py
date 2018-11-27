#############################################################################
#
# Is the Word an Isogram? 
##################
#
# An isogram is a word that has no repeating letters, consecutive or
# nonconsecutive. Create a function that takes a string and returns either True
# or False depending on whether or not it's an "isogram".
# 
# Notes
########
#  Ignore letter case (should not be case sensative).
#  All test cases contain valid one word strings.
#############################################################################

def is_isogram(txt):
    word = txt.lower()
    for i in word:
        if word.count(i) > 1:
            return False
    return True


