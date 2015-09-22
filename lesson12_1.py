"""
---------------------------------------------------------
Change Log
Author    Date:       Change:             Reason:
---------------------------------------------------------
Python Scripting Activity
For Instructor: 
Author: Ken Livesey
 
---------------------------------------------------------
Activity 1: Working with files

Using the lesson shell script and a text editor, create a Python script. Change the documentation to show you wrote the script.

This script should do the following: 
Use the os module and an if statement to determine if a directory exists and create a directory called c:\temp\mypythonfiles as needed (hint: use google/bing/yahoo to search for the syntax for os.path.isdir)
Create a file called plague_warning.txt in the directory that was just created
Write the text for the children's rhyme "Ring around the Rosie" to the file in multiple lines
Close the file

Save the script as Lesson12_1.py

Test the script in Python"""

# Import OS
import os

# Set Vars
CHK_PATH = "C:\\temp\\"
MK_DIR = "C:\\temp\\mypythonfiles"
NEW_FILE = MK_DIR + "\\plague_warning.txt"
FILE_DATA = "Ring around the Rosie\n"

# Check to see if the C:\temp directly exists if not make it so
if not (os.path.isdir(CHK_PATH)):
    os.makedirs(CHK_PATH)
else: print (CHK_PATH, "Exists")

# Check to see if the C:\temp\mypythonfiles directly exists if not make it so
if not (os.path.isdir(MK_DIR)):
    os.makedirs(MK_DIR)
else: print (MK_DIR, "Exists")

# Make a new file in mypythonfiles called plaque_warning.txt
MY_HNDL = open(NEW_FILE, "w")

# Write the text for the children's rhyme "Ring around the Rosie" to the file in multiple lines
for X in range(0, 20):
    MY_HNDL.write(FILE_DATA)

# Clost file
MY_HNDL.close