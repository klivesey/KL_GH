"""
---------------------------------------------------------
Change Log
Author    Date:       Change:             Reason:
---------------------------------------------------------
Python Scripting Activity
For Instructor: 
Author: Ken Livesey
 
---------------------------------------------------------
Activity 2: Adding to Lists

Using the lesson shell script and a text editor, create a Python script. Change the documentation to show you wrote the script.

This script should do the following: 
Create a variable called stuff_list and set it equal to an empty list
Add elements with the append() function to the list using the following:
Insert the last 5 years that you were in school as separate elements
Insert the last 3 amusement parks you went to as separate elements
Insert the last 3 movies you saw as separate elements (each movie title is an element)
Print the size of the list
Print the whole list

Save the script as Lesson11_2.py

Test the script in Python"""

# Set Var to null
STUFF_LIST = []

# Insert data - last 5 years of school
STUFF_LIST.append (1991)
STUFF_LIST.append (1992)
STUFF_LIST.append (1993)
STUFF_LIST.append (1994)
STUFF_LIST.append (2015)

# Insert data - last 3 amusement parks
STUFF_LIST.append ("Noahs Ark")
STUFF_LIST.append ("6 Flags") 
STUFF_LIST.append ("Mall of America")

# Insert data - last 3 movies
STUFF_LIST.append ("Frozen")
STUFF_LIST.append ("007") 
STUFF_LIST.append ("South Paw")

# Print the lenght of the list
print ("There are", len(STUFF_LIST), "elements in our list")

# Print the whole list
print ("\nOur list contains:", STUFF_LIST)

#End of Script