"""
---------------------------------------------------------
Change Log
Author    Date:       Change:             Reason:

--------------------------------------------------------- 
Python Scripting Activity
For Instructor: 
Author: Ken Livesey
 
---------------------------------------------------------


Activity 1: While loop

Using the lesson shell script and a text editor, create a Python script. Change the documentation to show you wrote the script.

This script should do the following: 
Print "While Loop follows:"
Create a variable called ndx and set it equal to 0
Create a while loop based on the condition that ndx is less than 100
Inside of the loop:
Print only the even indexes (hint... you can use the modulo operator) on separate lines
Don't forget to increment the index

Save the script as Lesson10_1.py

Test the script in Python"""

# Set Vars
NDX = 0

# Print init statement
print ("While loop follows:")

# While condition using a n + 2 method - do not show 100 result
while NDX < 100 :
    NDX = NDX +2
    print ("\n\t", NDX)
    if NDX >= 98 :
        break

# While condition using a modulo method pre increment 
while NDX < 100 :
    NDX = NDX +1
    if NDX % 2 == 0 :
	    print ("\n\t", NDX)
    if NDX >= 99 :
       break

# While condition using a modulo method post increment (zero product issue)
while NDX < 100 :
    if NDX % 2 == 0 and NDX != 0 :
	    print ("\n\t", NDX)
    NDX = NDX +1
    if NDX >= 99 :
        break

# End of Script




