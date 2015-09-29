'''
---------------------------------------------------------
Change Log
Author    Date:       Change:             Reason:
---------------------------------------------------------
Python Scripting Activity
For Instructor: 
Author: Ken Livesey
 
---------------------------------------------------------

Activity 1: Manipulating Services

Using the lesson shell script and a text editor, create a Python script. Change the documentation to show you wrote the script.

This script should do the following: 
Using the os.system() function, stop and restart the Windows Firewall service (hint: at the command-prompt, get help on net stop and net start
Using the os.system() function, stop and restart the Windows Defender service
Using the os.system() function, stop and restart the Windows Update service

Save the script as Lesson13_1.py

Test the script in Python
'''

# Import modules
import os
import sys


# Set Vars
NSTART = "net start "
NSTOP = "net stop "

# Get the service string from passed arguments
# MpsSvc = Windows Firewall
# WinDefend = Windows Defender
# wuauserv = Windows Updater
SVC = sys.argv[1]

# Build the command strings
CMD1 = NSTOP + SVC
CMD2 = NSTART + SVC

#Execute the service start and and stop commands in a subshell
os.system(CMD1)
os.system(CMD2)

# End of script

