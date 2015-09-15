"""
---------------------------------------------------------
Change Log
Author    Date:       Change:             Reason:

---------------------------------------------------------
Python Scripting Activity
For Instructor: 
Author: Ken Livesey
 
---------------------------------------------------------


Activity 1: Logical Conjunctions

Using the lesson shell script and a text editor, create a Python script. Change the documentation to show you wrote the script.

This script should do the following: 
Using sys module, accept 3 command-line inputs to the script and name them num1, num2, num3.
Compare the numbers for the following conditions:
When num1 and num2 is equal and num1 is less than num3, print "the first condition is TRUE"
When num1 is less than num2 and num1 is less than num3, print "the second condition is TRUE"
When num1 and num2 is equal and num3 is less than num2, print "the third condition is TRUE"
When num1 and num3 is equal or num1 is less than num3, print "the fourth condition is TRUE"
When num1 and num2 is equal or num1 is greater than num3, print "the fifth condition is TRUE"

Save the script as Lesson9_1.py

Test the script in Python"""

import sys

# Set Vars and change passed arguments to integers 

NUM1 = int(sys.argv[1])
NUM2 = int(sys.argv[2])
NUM3 = int(sys.argv[3])

# Condition 1 - When num1 and num2 is equal and num1 is less than num3, print "the first condition is TRUE"
if NUM1 == NUM2 and NUM1 < NUM3 :
    print ("\n\t The first condition is TRUE :", NUM1, "=", NUM2, "and", NUM1, "<", NUM3)

# Condition 2 - When num1 is less than num2 and num1 is less than num3, print "the second condition is TRUE"
if NUM1 < NUM2 and NUM1 < NUM3 :
    print ("\n\t The second condition is TRUE :", NUM1, "<", NUM2, "and", NUM1, "<", NUM3)

# Condition 3 - When num1 and num2 is equal and num3 is less than num2, print "the third condition is TRUE"
if NUM1 == NUM2 and NUM3 < NUM2 :
    print ("\n\t The third condition is TRUE :" , NUM1, "=", NUM2, "and", NUM3, "<", NUM2)

# Condition 4 - When num1 and num3 is equal or num1 is less than num3, print "the fourth condition is TRUE"
if NUM1 == NUM2 or NUM1 < NUM3 :
   print ("\n\t The forth condition is TRUE :" , NUM1, "=", NUM2, "or", NUM1, "<", NUM3)
  
# Condition 5 - When num1 and num2 is equal or num1 is greater than num3, print "the fifth condition is TRUE"
if NUM1 == NUM2 or NUM1 > NUM3 :
   print ("\n\t The fifth condition is TRUE :" , NUM1, "=", NUM2, "or", NUM1, ">", NUM3)

# End of Script




