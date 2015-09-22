"""
---------------------------------------------------------
Change Log
Author    Date:       Change:             Reason:
---------------------------------------------------------
Python Scripting Activity
For Instructor: 
Author: Ken Livesey
 
---------------------------------------------------------
Activity 2: Reading and writing files

Using the lesson shell script and a text editor, create a Python script. Change the documentation to show you wrote the script.

This script should do the following: 
Open the file created in the first script for read/write access
Create a for loop to print the contents of the file to the screen
Go to Wikipedia to obtain a 3 sentence definition for the Black Plague
Write the definition to the file
Close the file
Reopen the file for reading
Create a for loop to print the contents of the file to the screen
Close the file

Save the script as Lesson12_2.py

Test the script in Python"""

# Import OS
import os

# Set Vars
CHK_PATH = "C:\\temp\\"
MK_DIR = "C:\\temp\\mypythonfiles"
NEW_FILE = MK_DIR + "\\plague_warning.txt"
FILE_DATA = "Ring around the Rosie\n"
BLACK_STR = "The Black Death was one of the most devastating pandemics in human history, resulting in the deaths of an estimated 75 to 200 million people and peaking in Europe in the years 1346–53. Although there were several competing theories as to the etiology of the Black Death, analysis of DNA from victims in northern and southern Europe published in 2010 and 2011 indicates that the pathogen responsible was the Yersinia pestis bacterium, probably causing several forms of plague"


# Make a new file in mypythonfiles called plaque_warning.txt
MY_HNDL = open(NEW_FILE, "r+")

# Print contence of file
for x in MY_HNDL:
    print (x)

# Write 3 sentence Black Plague definition
MY_HNDL.write (BLACK_STR)

# Close file
MY_HNDL.close

# Open file with read access
MY_HNDL = open(NEW_FILE, "r")

# Print contense of file
for x in MY_HNDL:
    print (x)
