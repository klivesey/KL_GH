"""
---------------------------------------------------------
Change Log
Author    Date:       Change:             Reason:
---------------------------------------------------------
Python Scripting Activity
For Instructor: 
Author: Ken Livesey
 
---------------------------------------------------------
Activity 3: Working with files

Using the lesson shell script and a text editor, create a Python script. Change the documentation to show you wrote the script.

This script should do the following: 
Use the os module to execute dir \s c:\windows\system32 while redirecting to a file called c:\temp\mypythonfiles\dirout.txt
Open the file dirout.txt for reading
Create a loop to print the contents to the screen
Close the file

Save the script as Lesson12_3.py

Test the script in Python
"""

# Import OS
import os

# Set Vars
MK_DIR = "C:\\temp\\mypythonfiles"
NEW_FILE = MK_DIR + "\\dirout2.txt"
EXE = "dir"
ARGS = "\s c:\windows\system32"
DIR_OUT = " >" + NEW_FILE
CMD = EXE + ARGS + DIR_OUT
MY_HNDL = open(NEW_FILE, "w")
os.system(CMD)
 
print (CMD)
#MY_HNDL.close

