'''
---------------------------------------------------------
Change Log
Author    Date:       Change:             Reason:
---------------------------------------------------------
Python Scripting Activity
For Instructor: 
Author: Ken Livesey
 
---------------------------------------------------------

Activity 2: Drive scan

Using the lesson shell script and a text editor, create a Python script. Change the documentation to show you wrote the script.

This script should do the following: 
Using the os.system() function, schedule a chkdsk scan on the c: drive
Using the os.system() function, schedule a shutdown and restart of the workstation with a delay of 30 seconds and by forcibly closing all applications

Save the script as Lesson13_2.py

Test the script in Python
'''

# Import modules
import os

# Set command vars
TR1 = "\"chkdsk c:\""
TR2 = "\"shutdown /f /r /t 30\""

# Set Task Scheduler command
STSK1 = "schtasks /create /TN DSKScan /SC DAILY /ST 20:00 /TR "
STSK2 = "schtasks /create /TN PMShut /SC DAILY /ST 21:00 /TR "

# Build the command strings
CMD1 = STSK1 + TR1
CMD2 = STSK2 + TR2

#Execute the schedule commands in a subshell
os.system(CMD1)
os.system(CMD2)

# End of script

