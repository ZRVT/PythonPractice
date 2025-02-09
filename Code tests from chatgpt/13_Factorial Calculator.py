def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result
# this for loop i did not do myself, i have had difficulties understandign this for loop for a while now. 

while True:
    #This while loop will validate the input to ensure the right valid is added
    try:
        number = int(input("Input integer: "))
        if number > 0:
            break
        else:
            print('Please input a positive number')
    except ValueError:
        print('Please input valid integer!')

print(f'The factorial of {number} is: {factorial(number)}')