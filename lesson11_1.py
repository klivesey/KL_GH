"""
---------------------------------------------------------
Change Log
Author    Date:       Change:             Reason:
---------------------------------------------------------
Python Scripting Activity
For Instructor: 
Author: Ken Livesey
 
---------------------------------------------------------
Activity 1: Creating Lists

Using the lesson shell script and a text editor, create a Python script. Change the documentation to show you wrote the script.

This script should do the following: 
Create a variable called comp_list and set it equal to a list with the following values: CPU, RAM, GPU, USB, LCD
Using print() and the appropriate index, print the second element
Using print() and the appropriate index, print the fourth element
Using print() and len(), print the size of the list

Save the script as Lesson11_1.py

Test the script in Python"""

# Set Var to list of strings
COMP_LIST = ["CPU", "RAM", "GPU", "USB", "LCD"]

# Print The second elemtent of the list
print (COMP_LIST[1])

# Print The second elemtent of the list
print (COMP_LIST[3])

# Prient the length of the list
print (len(COMP_LIST))

#End of Script