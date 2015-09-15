"""
---------------------------------------------------------
Change Log
Author    Date:       Change:             Reason:
---------------------------------------------------------
Python Scripting Activity
For Instructor: 
Author: Ken Livesey
---------------------------------------------------------

Activity 2: More interactive fun

Using the lesson shell script and a text editor, create a Python script. Change the documentation to show you wrote the script.

This script will take the user's name and 3 separate grades. It will then average the grades and print the result. This script should do the following: 
Using the sys module, accept 4 command-line arguments to the script and assign the argument values to 4 variables which will be named my_name, test1, test2, test3
Calculate the average grade and set it equal to a variable called average. You may need to covert the data types of the argument values in order to perform the requisite mathematics. See the sample code.
Print the message "The test average for name is average".
Test the script a few times with different data

Save the script as Lesson7_2.py

Test the script in Python""

import sys


if len(sys.argv) != 1:
   print ("Please pass one input argument")
   sys.exit(1)
"""
import sys

# Set Vars and change passed arguments to integers 
MY_NAME = sys.argv[1]
TEST1 = int(sys.argv[2])
TEST2 = int(sys.argv[3])
TEST3 = int(sys.argv[4])

SUM = (TEST1, TEST2, TEST3)

AVGERAGE = round(sum(SUM)/len(SUM),2)

print ("The test average for", MY_NAME, "is", AVGERAGE)

