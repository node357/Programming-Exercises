#############################################################################
#
# ATM PIN Code Validation 
##################
#
# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain
# anything but exactly 4 digits or exactly 6 digits. Your task is to create a
# function that takes a string and returns True if the PIN is valid and False
# if it's not.
#
# Notes
#   Some test cases contain special characters.
#   Empty strings must return False.
#############################################################################

def is_valid_PIN(pin):
    if len(pin) in [4, 6]:
        for p in pin:
            if p.isdigit():
                return True
            else:
                return False
    return False

# More pythonic

def is_valid_PIN(pin):
    return len(pin) in [4,6] and pin.isdigit()









