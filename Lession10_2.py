"""
---------------------------------------------------------
Change Log
Author    Date:       Change:             Reason:

---------------------------------------------------------
Python Scripting Activity
For Instructor: 
Author: Ken Livesey
 
---------------------------------------------------------


Using the lesson shell script and a text editor, create a Python script. Change the documentation to show you wrote the script.

This script should do the following: 
Print "For Loop follows:"
Create a for loop based on the conditions that the index is initialized to 0, ndx is less than 26, and the index is incremented by 1
For each iteration, print the current letter of the alphabet. Start at the letter A. Thus, for each iteration, a single letter is printed on a separate line. (hint... you can use an elif tree, research ASCII codes, or use another method you derive)

Save the script as Lesson10_2.py

Test the script in Python"""

# Set Vars
NDX = 0

# Print init statement
print ("For loop follows:")

# Set a list of alphabet characters
ALPH = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Count the characters of the alphabet (our high range) 
ALPH_LEN = len(ALPH)

# For loop which matches and prints corresponding alphabet characters 
for X in range(0, ALPH_LEN):
    print(ALPH[X])

# Again with spaces and tabs
print ("\nFor loop follows:")
for X in range(0, ALPH_LEN):
    print("\n\t", ALPH[X])

#End of Script


