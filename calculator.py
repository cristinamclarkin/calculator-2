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
        #slice off numbers and convert to floats
        nums = map(float, tokens[1:])
        if len(tokens) > 2:
            if tokens[0]== "+": #if/elif/else arithmetic signs
                print add(nums)
            elif tokens[0] == "-":
                print subtract(nums)
            elif tokens[0] == "*":
                print multiply(nums)
            elif tokens[0] == "/":
                print divide(nums)
            elif tokens[0] == "pow":
                print power(nums)
            else:
                print mod(nums)
        
        elif len(tokens) <= 2:
            if tokens[0] == "square":
                print square(nums)
            elif tokens[0] == "cube":
                print cube(nums)
        

calculator()