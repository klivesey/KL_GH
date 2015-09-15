"""
---------------------------------------------------------
Change Log
Author    Date:       Change:             Reason:

---------------------------------------------------------
Python Scripting Activity
For Instructor: 
Author: Ken Livesey
 
---------------------------------------------------------

Activity 1: Simple input

Using the lesson shell script and a text editor, create a Python script. Change the documentation to show you wrote the script.

This script should do the following: 
Create a variable and name it street. Assign "1600 Pennsylvania Avenue" to the variable.
Print the variable
Accept input from a user
Using the input() function, accept input from the user and put it into a variable called address
Print "You live at address" on another line

Save the script as Lesson7_1.py

Test the script in Python"""

# Set Vars
STREET = "1600 Pennsylvania Avenue"
print (STREET)

# Capture and display user input
ADDRESS = input("What is your address? ")
print ("You live at address: ", ADDRESS)


