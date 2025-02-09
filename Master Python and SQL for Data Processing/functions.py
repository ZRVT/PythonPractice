def squared(x: int) -> int: 
    """This function will square the argument and return it.

    Args:
        x (int): Received an argument that will be squared

    Returns:
        int: Returns the squared value of the argument. 
    """
    y = x ** 2
    return y
print(squared(15))

def pow(x:int, times:int) -> int:
    """_summary_

    Args:
        x (int): value that be used
        times (int): the amount of times

    Returns:
        int: the pow of the x value
    """
    return x ** times
print(pow(3,2))

assert pow(3,2) == squared(3)