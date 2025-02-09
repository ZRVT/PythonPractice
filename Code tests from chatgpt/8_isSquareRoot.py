def square():
    while True:
        try:     
            userInput = float(input('Enter a number: '))
            return userInput ** 2
        except ValueError:
            print("please provide a valid number")

result = square()

print(f'The square is: {result}')