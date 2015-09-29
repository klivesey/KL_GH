'''
---------------------------------------------------------
Change Log
Author    Date:       Change:             Reason:
---------------------------------------------------------
Python Scripting Activity
For Instructor: 
Author: Ken Livesey
 
---------------------------------------------------------

Activity 3: Interactive Drive scan

Using the lesson shell script and a text editor, create a Python script. Change the documentation to show you wrote the script.

This script should do the following: 
Copy the script from Activity 2 and rename the copied script to Lesson13_3.py
Edit the script to use the input() function to query the user for the timeout period
Edit the script to use another input() function to query the user for a message to display as the machine executes the shutdown

Save the script as Lesson13_3.py

Test the script in Python

'''

# Import modules
import os
import sys
import shutil

# Set file copy string vars 
SRC = "C:\pythonscripts\lesson13_2.py"
DST = "C:\pythonscripts\lesson13_3a.py"

# Copy file
shutil.copyfile(SRC, DST)

# Get some input and set vars
TOUT = input("Number of seconds to delay before shutdown? ")
S = input("Enter a system shutdown prompt: ")

# Add the switch to display comments
MSG = " /c " + S

# Set command string
TR = "\"shutdown /f /r /t " + TOUT + MSG + "\"" 

# Set Task Scheduler command
STSK = "schtasks /create /TN PMShut /SC DAILY /ST 21:00 /TR "

# Build the command strings
CMD = STSK + TR

#Execute the schedule commands in a subshell
os.system(CMD)

# End of script

