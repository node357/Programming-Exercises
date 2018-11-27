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
"""
Creates an object which allows a user to input a string, composed of either a range of integers between 1-9 or a list of roman numerals.
"""

class Converter:

    def __init__(self, value):
        self.value = value
        self.numerals = ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
        self.decimals = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)

        if len(self.value) == 0:
            raise ValueError("[!] No Characters Detected")

    def Convert_to_roman(self):

        if not self.value.isdigit() or self.value.startswith("0"):
            raise ValueError("Integers 1-9 Only")

        self.value = int(self.value)
        self.result = []

        for i in range(len(self.numerals)):
            count = int(self.value / self.decimals[i])
            self.result.append(self.numerals[i] * count)
            self.value -= self.decimals[i] * count

        return "".join(self.result)

    def Convert_to_integer(self):

        self.value = self.value.upper()
        self.numeral_ints = dict(zip(list(self.numerals), list(self.decimals)))

        result = 0
        for i in range(len(self.value)):
            try:
                value = self.numeral_ints[self.value[i]]
                if i+1 < len(self.value) and self.numeral_ints[self.value[i+1]] > value:
                    result -= value
                else:
                    result += value
            except KeyError:
                raise ValueError("Invalid Numeral Detected")
        return result

if __name__ == "__main__":
    mein = Converter("XLV")

    print(mein.Convert_to_integer())
