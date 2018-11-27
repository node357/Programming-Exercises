#############################################################################
#
# Pi to N Decimal Places
##################
#
# Given a number n, write a function that returns PI to n decimal places.
#
#############################################################################

def my_pi(n):
    try:
        from math import pi
        if n <= 15:
            return round(pi, n)
        else:
            pass
    except:
        pass

if __name__ == "__main__":
    print(my_pi(16))

