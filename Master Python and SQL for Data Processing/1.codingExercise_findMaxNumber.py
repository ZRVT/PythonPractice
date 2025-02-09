""" Here we will find the max number"""
def find_max_numbers(numbers) -> int:
    """Function to fine max number of a list

    Args:
        numbers: list of numbers

    Returns:
        int: returns the highest number or none. 
    """
    if numbers:
        return max(numbers)
    else:
        return None
    
listNum = [5, 9, 2, 12, 7]
print(find_max_numbers(listNum))

""" Here we will make a string mutation for test 2"""
def greet(name: str, age: int) -> str:
    return f'{name}! you are {age} years old.'

print(greet('Zino',31))

"""Here we are checking if a number is even or not."""
def is_even(num):
    if num % 2 == 1:
        return False
    else:
        return True
print(is_even(0))

""" """
def factorial(n):
    result = 1 # something we will add to
    for i in range(1,n + 1):
        result *= i
        print(result)
    return result

factorial(1)