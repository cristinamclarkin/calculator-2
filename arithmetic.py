def add(nums): 
    result = 0
    for num in nums:
        result = result + num 
    return result 

def subtract(nums):
    result = nums[0]
    for num in nums[1:]:
        result = result - num
    return result

def multiply(nums):
    result = 1
    for num in nums:
        result = result * num
    return result


def divide(nums):
    # Need to turn at least numument to float for division to
    # not be integer division
    result = float(nums[0])
    for num in nums[1:]:
        result = result / num
    return result

def square(nums):
    # Needs only one numument
    for num in nums:
        result = num * num
    return result

def cube(nums):
    # Needs only one numument
    for num in nums:
        result = num * num * num
    return result

def power(nums):
    result = nums[0]
    for num in nums[1:]:
        result = result ** num
    return result

def mod(nums):
    result = nums[0]
    for num in nums[1:]:
        result = result % num
    return result
