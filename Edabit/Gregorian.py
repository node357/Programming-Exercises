#############################################################################
#
# Gregorian Calendar 
##################
#
# Write a function to return the name of the month as a string when provided an
# integer representing the month on the Gregorian calendar. Use the below table
# for reference. You can expect all test cases to provide a valid integer
# input.
#
#############################################################################

def month_name(num):

    """
    months = {"1".zfill(2) :	"January",
              "2".zfill(2) :    "February",
	      "3".zfill(2) :	"March",
	      "4".zfill(2) :	"April",
	      "5".zfill(2) :	"May",
	      "6".zfill(2) :    "June",
	      "7".zfill(2) :	"July",
	      "8".zfill(2) : 	"August",
	      "9".zfill(2) : 	"September",
	       10 	   : 	"October",
	       11          :	"November",
	       12          : 	"December"
					}
    if months.has_key(num):
        return months[num]
    else:
    	pass
    return months[num]
    """
    months = {1 : "January",
              2 : "February",
	      3 : "March",
	      4 : "April",
	      5 : "May",
	      6 : "June",
	      7 : "July",
	      8 : "August",
	      9 : "September",
	      10: "October",
	      11: "November",
	      12: "December"
	}
    return months[num]
	
print(month_name(2))

			
