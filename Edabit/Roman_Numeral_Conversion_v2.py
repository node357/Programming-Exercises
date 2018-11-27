####################################################################################
#
# Challenge Name: Roman Numeral Conversion
# Challenge URL: https://bit.ly/2AYJOJ0
#
# Challenge Description
#######################
# Create a function that will take either a string containing a roman numeral,
# or an integer.
#
# Given a numeral, return the integer value of that roman numeral.
# Given an integer, return the equivalent roman numeral.
#
# Roman Numeral Rules
#####################
#
# 1) I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000.
# 2) Zero is not represented.
# 3) Numbers greater than 3,999 are not represented.
#
# 4) Roman numerals are repeated to add value:
#    III is equivalent to 1 +1 +1 = 3.
#
# 5) Only powers of 10 may be repeated in this way.
#    Thus, VV is invalid; 5 + 5 would instead be
#    expressed as X.
#
# 6) No more than three repetitions of a numeral can be used.
#    Five repetitions can be represented with a single, larger numeral;
#    to represent four, use the next larger numeral, but precede it
#    with a numeral to subtract from it.
#
#    Thus, IIII is invalid and would instead be written as IV (one less than five).
#    Likewise, XC represents 90 (10 less than 100), and XL represents 40
#    (10 less than 50).
#
# 7) A numeral used for subtraction in this way must be the largest power of 10
#    that is less than the numeral it precedes. Thus, XC is valid but IC is invalid.
#
####################################################################################

def roman_numerals(arg):

    numerals = ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
    decimals = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)

    if isinstance(arg, str) and len(arg) != 0:
        arg = arg.upper()
        numeral_ints = dict(zip(list(numerals), list(decimals)))

        result = 0
        for i in range(len(arg)):
            try:
                value = numeral_ints[arg[i]]
                if i+1 < len(arg) and numeral_ints[arg[i+1]] > value:
                    result -= value
                else:
                    result += value
            except KeyError:
                raise ValueError("Invalid Numeral Detected")
        return result


    if isinstance(arg, int) and int(arg) != 0:
        arg = int(arg)
        result = []
        for i in range(len(numerals)):
            count = int(arg / decimals[i])
            result.append(numerals[i] * count)
            arg -= decimals[i] * count
        return "".join(result)

if __name__ == "__main__":
    print(roman_numerals("I"))
