# Activity 1: Commands
#
#Create a simple text file using Windows Notepad
#
#This script should do the following: 
#Type the command to change to the C drive
C:

#Type the command to create a directory called c:\pythonscripts
MD C:\pythonscripts

#Type the command to list the complete contents of the windows directory
DIR c:\windows

#Type the command to redirect the listing of the complete contents of the windows directory to a file called c:\pythonscripts\mylisting.txt
DIR c:\windows > c:\pythonscripts\mylisting.txt

#Type the command to redirect the listing of the contents of the root of the C drive to append to c:\pythonscripts\mylisting.txt
DIR c: >> c:\pythonscripts\mylisting.txt

#Type the command to redirect the output of the help command to append to c:\pythonscripts\mylisting.txt
HELP >> c:\pythonscripts\mylisting.txt

#Type the command to redirect the help information for shutdown to c:\pythonscripts\shutdown_help.txt
SHUTDOWN /? > c:\pythonscripts\shutdown_help.txt

#Type the command to redirect the help information for tasklist to c:\pythonscripts\tasklisting_help.txt
TASKLIST /? > c:\pythonscripts\tasklisting_help.txt

#Type the command to redirect the help information for taskkill to c:\pythonscripts\taskkilling_help.txt
TASKKILL /? > c:\pythonscripts\taskkilling_help.txt

#Type the command to redirect the help information for chkdsk to c:\pythonscripts\chkdsking_help.txt
CHKDSK /? > c:\pythonscripts\chkdsking_help.txt

#Type the command to redirect the help information for openfiles to c:\pythonscripts\openfiling_help.txt
OPENFILES /? > c:\pythonscripts\openfiling_help.txt

#Type the command to redirect the help information for schtasks to c:\pythonscripts\openfiling_help.txt
SCHTASKS /? > c:\pythonscripts\openfiling_help.txt

#Type the command to type the contents of c:\pythonscripts\mylisting.txt to the screen
TYPE c:\pythonscripts\mylisting.txt

#Type the command to delete c:\pythonscripts\mylisting.txt
DEL c:\pythonscripts\mylisting.txt
