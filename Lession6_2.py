"""
---------------------------------------------------------
Change Log
Author    Date:       Change:             Reason:

---------------------------------------------------------
Python Scripting Activity
For Instructor: 
Author: Ken Livesey
 
---------------------------------------------------------

Activity 2: More variable fun

Using the lesson shell script and a text editor, create a Python script. Change the documentation to show you wrote the script.

This script should do the following: 
	Create a variable and name it housenum. Assign it a value of 5.
	Print housenum on a separate line.
	Change the value of housenum by multiplying the variable by 12
	Print housenum on a separate line.
	Change the value of housenum by subtracting 3 using using compound assignment.
	Print housenum on a separate line.

Save the script as Lesson6_2.py

Test the script in Python"""

#Create a variable and name it housenum. Assign it a value of 5
HOUSENUM = 5
print (HOUSENUM)

#Change the value of housenum by multiplying the variable by 12
HOUSENUM = HOUSENUM * 12
print (HOUSENUM)

#Change the value of housenum by subtracting 3 using using compound assignment
HOUSENUM -= 3
print (HOUSENUM)