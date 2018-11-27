#############################################################################
#
# Count the Letters and Digits 
##################
#
# Write a function that takes a string and calculates the number of letters and
# digits within it. Return the result in a dictionary.
#
#############################################################################
import math 

def count_all(txt):
    letters = 0
    digits = 0
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in txt:
        if i.isdigit():
            digits += 1
        elif i in alphabet:
            letters += 1

    return {"LETTERS" : letters, "DIGITS" : digits}



def count_all(txt):
    result = {"LETTERS" : 0, "DIGITS" : 0}
    for i in txt:
        if i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            result["LETTERS"] += 1
        elif i.isdigit():
            result["DIGITS"] += 1
        else:
            
    return result

print(count_all("  "))


def count_all(txt):

