"""
---------------------------------------------------------
Change Log
Author    Date:       Change:             Reason:

---------------------------------------------------------
Python Scripting Activity
For Instructor: 
Author: Ken Livesey
 
---------------------------------------------------------

Activity 2: Simple printing with line breaks

Using the lesson shell script and a text editor, create a Python script. Change the documentation to show you wrote the script.

This script should do the following: 
Print the last 3 movies that you saw in the theatre. Separate each movie with a blank line.
Print the last 3 software titles that you purchased. Separate each software with 2 blank lines.
Print your 3 favorite meals. Separate each meal with 3 blank lines.

Save the script as Lesson4_2.py

Test the script in Python """

# Set Vars
MOVIES = ["The Hobbit", "South Paw", "Inside Out"]
STITLE = ["NordVPN", "Office 2013", "Ninite Updater"]
MEALS = ["Tom's Ribeyes", "Fresh BLT's", "Christmas Lasagna"]
STR1 = "The last three movies I attended are:"
STR2 = "The last three software programs I purchased are:"
STR3 = "My top three favorite meals are:"

# List last three movies with single spaces in between
print (STR1)
for X in MOVIES:
        print(X + "\n")

# List last three software purchases with double spaces in between
print (STR2)
for X in STITLE:
        print(X + "\n\n")


# List top three meals with double spaces in between
print (STR3)
for X in MEALS:
        print(X +"\n\n\n")


# end of script
