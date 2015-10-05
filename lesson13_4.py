'''
---------------------------------------------------------
Change Log
Author    Date:       Change:             Reason:
---------------------------------------------------------
Python Scripting Activity
For Instructor: 
Author: Ken Livesey
 
---------------------------------------------------------

Activity 4: Functions

Using the lesson shell script and a text editor, create a Python script. Change the documentation to show you wrote the script.
In the text in Chapter 3, pg. 21 - 24, you will find a description for creating functions. In this activity you will create 3 script functions and call them from within your script
Additionally, view sample code #13 on BlackBoard for working samples of functions

This script should do the following: 

    1.  Create a function called calc_area to calculate the area from two numbers
    2.  Create a function definition with 2 variables called x and y
    3.  calculate the area and assign to a variable called z
    4.  print z to the screen in a descriptive statement
    5.  Create a function called calc_square to calculate the square from a number
    6.  create a function definition with 1 variable called x
    7.  calculate the square and assign to a variable called sq
    8.  print sq to the screen in a descriptive statement
    9.  Create a function called do_logoff to calculate the logoff the user from the workstation (hint... be sure to save your work before testing)x
    10  Use the os.system() to call logoff.exe to close the session
    12. In the script body (outside of any function), query the user using the input() function to select which function to invoke
        (1-area,2-square, 3-logoff)
    13. Assign the user's response to a variable
    14. Using an if statement, if the user typed a 1 then invoke the area function
    15. Create 2 additional functions to handle the other 2 options

Save the script as Lesson13_3.py

Test the script in Python

'''

# Import modules
import os
import sys

# Part 1
#    1.  Create a function called calc_area to calculate the area from two numbers
#    2.  Create a function definition with 2 variables called x and y
#    3.  calculate the area and assign to a variable called z
#    4.  print z to the screen in a descriptive statement
def calc_area(x, y) :
    Z = x * y
    return Z

def print_area () :    
    Z = str(calc_area (8, 25))    
    PNT = "The Area of a 8x25\' equiangular polygon is " + Z + " feet."
    print (PNT)

# Part 2
#    5.  Create a function called calc_square to calculate the square from a number
#    6.  create a function definition with 1 variable called x
#    7.  calculate the square and assign to a variable called sq
#    8.  print sq to the screen in a descriptive statement
def calc_square (x) :
    return x * x

def print_square () :
    SQ = str(calc_square (8))
    PNT = "The square of 8 is " + SQ
    print (PNT)

# Part 3
#    9.  Create a function called do_logoff to logoff the user from the workstation (hint... be sure to save your work before testing)x
#    10  Use the os.system() to call logoff.exe to close the session
def logoff () :
    x = "shutdown /l"
    print ("User would have been logged out via the command: os.system(" + x + ")")

def print_logoff () :
    logoff ()

# Part 4
#    12. In the script body (outside of any function), query the user using the input() function to select which function to invoke (1-area,2-square, 3-logoff)
#    13. Assign the user's response to a variable
#    14. Using an if statement, if the user typed a 1 then invoke the area function
VAR1 = int(input("Select which function to invoke - (1-area, 2-square, 3-logoff) "))
if VAR1 == 1 :
    print_area()

if VAR1 == 2 :
    print_square ()

if VAR1 == 3 :
    logoff ()


