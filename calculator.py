"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


def calculator(): #initialize loop that will execute given block of code
    """calculator funtion
    takes a user input and executes arithmetic.py
    """
    while True: 
        user_input = raw_input(">")#takes input from user  
        if user_input == "q": # if q, quit (return none)
            return None
        tokens = user_input.split(" ") #tokenize input based on (" ")
        tokens[1] = float(tokens[1]) #convert strings to integers
        
        if len(tokens) > 2:
            tokens[2] = float(tokens[2])
            if tokens[0]== "+": #if/elif/else arithmetic signs
                print add(tokens[1], tokens[2])
            elif tokens[0] == "-":
                print subtract(tokens[1], tokens[2])
            elif tokens[0] == "*":
                print multiply(tokens[1], tokens[2])
            elif tokens[0] == "/":
                print divide(tokens[1],tokens[2])
            elif tokens[0] == "pow":
                print power(tokens[1],tokens[2])
            else:
                print mod(tokens[1], tokens[2])
        
        elif len(tokens) <= 2:
            if tokens[0] == "square":
                print square(tokens[1])
            elif tokens[0] == "cube":
                print cube(tokens[1])
        

calculator()