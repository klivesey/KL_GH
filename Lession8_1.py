"""
---------------------------------------------------------
Change Log
Author    Date:       Change:             Reason:

---------------------------------------------------------
Python Scripting Activity
For Instructor: 
Author: Ken Livesey
 
---------------------------------------------------------

Activity 1: Comparing Numbers

Using the lesson shell script and a text editor, create a Python script. Change the documentation to show you wrote the script.

This script should do the following: 
    Use sys module to accept 2 command-line inputs to the script (as the script is invoked) and name them num1, num2.
    Use if/else statements to print "the numbers are EQUAL" when the variables are equal or "the numbers are NOT EQUAL" when the variables are not equal.
    Use an if-statement to print "the first number is LESS" when the first number is less than the second.
    Use another if-statement to print "the second number is LESS" when the second number is less than the first.

Save the script as Lesson8_1.py

Test the script in Python"""

import sys

# Set Vars and change passed arguments to integers 

NUM1 = int(sys.argv[2])
NUM2 = int(sys.argv[3])

# Test the two arguments to see if they are equal
if NUM1 == NUM2:
    print ("The numbers are EQUAL")
else:
    print ("The numbers are not EQUAL")

# Test the to arguments to see if the first number is less
if NUM1 < NUM2:
    print ("The first number is LESS")

# Test the to arguments to see if the second number is less
if NUM1 > NUM2:
    print ("The second number is LESS")



