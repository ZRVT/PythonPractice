def stringy(size):
    if not isinstance(size, int) or size < 0:
        raise ValueError("Input must be a non-negative integer.")
    return ''.join('1' if i % 2 == 0 else '0' for i in range(size))

# Test
print(stringy(4))  # "1010"

# Ensure the input is a string 
#if size = 4 return "101010"
#if size = 12 return "101010101010"
#Force int() and make a function to ensure the input is an integer and a positive number