###################################################################
#
# Are Letters in the Second String Present in the First String?
################################################################
#
# Create a function that accepts a list of two strings and checks if the
# letters in the second string are present in the first string.
#
###################################################################

def letter_check(lst):
    cnt = 0
    j = lst[0].replace(" ", "").lower()
    o = lst[1].replace(" ", "").lower()
    for i in o :
        if i in j:
            cnt += 1
    if len(o) == cnt:
        return True
    else:
        return False

