def add(*args):
    result = 0
    for arg in args:
        result = result + arg 
    return result 

def subtract(*args):
    for arg in args:
        result = arg[0] - add(arg[1:])
    return result

def multiply(*args):
    return num1 * num2


def divide(*args):
    # Need to turn at least argument to float for division to
    # not be integer division
    return float(num1) / float(num2) 


def square(*args):
    # Needs only one argument
    return num1 * num1


def cube(*args):
    # Needs only one argument
    return num1 * num1 * num1


def power(*args):
    return num1 ** num2  # ** = exponent operator


def mod(*args):
    return num1 % num2
