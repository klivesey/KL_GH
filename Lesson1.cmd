#
# Activity 1: Commands
#
# Create a simple text file using Windows Notepad
#
# This script should do the following: 
# Type the command to list the commands with descriptions
HELP

# Type the command to list the help information for the shutdown command
SHUTDOWN /?

# Type the command to change to the C drive
C:

# Type the command to list all of the subdirectories of c:\window\system32
DIR c:\windows\system32

# Type the command to create a directory called c:\pythonscripts
MD c:\pythonscripts

# Type the command to create a directory called c:\temp\myfiles
MD c:\temp\myfiles

# Type the command to create a directory called lesson1 inside of myfiles
MD c:\temp\myfiles\lesson1

# Type the command to copy all of the .txt files found in Program Files to c:\temp\myfiles\lesson1
Copy "c:\program files\*.txt" c:\temp\myfiles\lesson1

# Type the command to change directory to c:\temp\myfiles
CD c:\temp\myfiles

# Without using a fully qualified path, type the command to completely delete the lesson1 directory
CD c:\temp\myfiles
RD lesson1 /s

# Type the command to change directory to the parent directory
CD ..

# Without using a fully qualified path, type the command to delete the myfiles directory
RD myfiles


# Save the script as Lesson1_1.bat in the pythonscripts directory on the C drive. This creates a command that you can invoke at the command prompt.
# At the command prompt, you can invoke the bat file by typing the fully qualified name to the file
# Be sure to copy your file to a safe location to refer back to later
#
# Test the script

