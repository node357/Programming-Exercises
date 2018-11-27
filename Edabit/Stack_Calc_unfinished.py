#############################################################################
#
# Stack Calculator 
##################
# 
# A stack machine processes instructions by pushing and popping values to an
# internal stack.
# A simple example of this is a calculator.

# The argument passed to run(instructions) will always be a string containing a
# series of instructions.
# The instruction set of the calculator will be this:

# +: Pop the last 2 values from the stack, add them, and push the result
#    onto the stack.
# -: Pop the last 2 values from the stack, subtract the lower one
#    from the topmost one, and push the result.
# *: Pop the last 2 values, multiply, and push the result.
# /: Pop the last 2 values, divide the topmost one by the
#    lower one, and push the result.
# DUP: Duplicate (not double) the top value on the stack.
# POP: Pop the last value from the stack and discard it.
# PSH: Performed whenever a number appears as an
#      instruction. Push the number to the stack.
#
# Any other instruction (for example, a letter) should result in the value "
# Invalid instruction: [instruction]"
#
#
#############################################################################

import re 

class StackCalc:
    
    def __init__(self):
        pass

    def run(self, instructions):

	




        try:

    	 #  +: Pop the last 2 values from the stack, add them, 
	 #     and push the result onto the stack.
	 l = [value for value in instructions.split





        except ValueError:

            return "Invalid instruction: {}".format(instructions)


    def getValue(self):
        pass

#
#
