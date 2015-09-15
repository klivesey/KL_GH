"""
---------------------------------------------------------
Change Log
Author    Date:       Change:             Reason:

---------------------------------------------------------
Python Scripting Activity
For Instructor: 
Author: Ken Livesey
 
---------------------------------------------------------

Activity 2: Comparing Strings

Using the lesson shell script and a text editor, create a Python script. Change the documentation to show you wrote the script.

This script should do the following: 
    Using the input() function, print "First address: " to the operator asking for a street address.
    Store the string in a variable called address1.
    Print "Second address: " to the operator asking for another street address.
    Store the string in a variable called address2.
    Use if/else statements to print "The addresses are EQUAL" when the variables are equal and "The addresses are NOT EQUAL" when the variables are not.
    If the addresses are not equal (within the else-block thereby creating a nested condition):
    Print "State for second address: " to the operator asking for the state for the second address.
    Store the string in a variable called state.
    Print "Zipcode for second address: " to the operator asking for the zip code for the second address.
    Store the number in a variable called zipcode.
    In a readable string, print "Street: address" replacing the word address with the variable for the second address.
    In a readable string, print "State: state" replacing the word state with the variable for the state.
    In a readable string, print "Zipcode: zipcode" replacing the word zipcode with the variable for the zipcode.

Save the script as Lesson8_2.py

Test the script in Python"""
# Prompt for input
ADDRESS1 = input("First address: ")
ADDRESS2 = input("Second address: ")

# Check to see if input strings are equal
if ADDRESS1 == ADDRESS2:
    print ("The addresses are EQUAL")
else:
    print ("The addresses are NOT EQUAL")
    STATE = input("State for second address: ")
    ZIPCODE = input("Zipcode for second address: ")
    print ("\n\tStreet:", ADDRESS2, "\n\tState:", STATE, "\n\tZipcode:", ZIPCODE)