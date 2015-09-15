"""
---------------------------------------------------------
Change Log
Author    Date:       Change:             Reason:

---------------------------------------------------------
Python Scripting Activity
For Instructor: 
Author: Ken Livesey
 
---------------------------------------------------------


Activity 2: Using elif in logical conjunctions

Using the lesson shell script and a text editor, create a Python script. Change the documentation to show you wrote the script.

This script should do the following: 
Using the sys module, accept 1 command-line input to the script and name it num1.
Using elif blocks:
If num1 is less than 12, print "the first condition is TRUE"
If num1 is equal to 19, print "the second condition is TRUE"
If num1 is greater than 19 and num1 is less than 31, print "the third condition is TRUE"
If num1 is greater than or equal to 42 and num1 is less than 100 , print "the fourth condition is TRUE"

Save the script as Lesson9_2.py

Test the script in Python"""

import sys

# Set Vars and change passed arguments to integers 
NUM1 = int(sys.argv[1])

# Condition 1 - If num1 is less than 12, print "the first condition is TRUE"
if NUM1 < 12 :
    print ("\n\t The first condition is TRUE :", NUM1, "< 12")
# Condition 2 - If num1 is equal to 19, print "the second condition is TRUE"
elif NUM1 == 19 :
    print ("\n\t The second condition is TRUE :", NUM1, "= 19")
# Condition 3 - If num1 is greater than 19 and num1 is less than 31, print "the third condition is TRUE"
elif NUM1 > 19 and NUM1 < 31 :
    print ("\n\t The third condition is TRUE :", NUM1, "> 19 and", NUM1, "< 31")
# Condition 4 - If num1 is greater than or equal to 42 and num1 is less than 100 , print "the fourth condition is TRUE"
elif NUM1 >= 42 and NUM1 < 100 :
    print ("\n\t The forth condition is TRUE :", NUM1, ">= 42", "and", NUM1, "< 100")

# End of Script




