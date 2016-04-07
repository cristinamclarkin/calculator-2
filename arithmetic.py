def add(*args): 
    result = 0
    for arg in args:
        result = result + arg 
    return result 

def subtract(*args):
    result = args[0]
    for arg in args[1:]:
        result = result - arg
    return result

def multiply(*args):
    result = 1
    for arg in args:
        result = result * arg
    return result


def divide(*args):
    # Need to turn at least argument to float for division to
    # not be integer division
    result = float(args[0])
    for arg in args[1:]:
        result = result / arg
    return result

def square(*args):
    # Needs only one argument
    for arg in args:
        result = arg * arg
    return result

def cube(*args):
    # Needs only one argument
    for arg in args:
        result = arg * arg * arg
    return result

def power(*args):
    result = args[0]
    for arg in args[1:]:
        result = result ** arg
    return result

def mod(*args):
    result = args[0]
    for arg in args[1:]:
        result = result % arg
    return result
