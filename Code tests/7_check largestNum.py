# while True: 
#     try:
#         num1 = float(input('Please enter a number: '))
#         break
#     except ValueError:
#         print('Please provide a valid number')

# while True: 
#     try:
#         num2 = float(input('Please enter a number: '))
#         break
#     except ValueError:
#         print('Please provide a valid number')

# while True: 
#     try:
#         num3 = float(input('Please enter a number: '))
#         break
#     except ValueError:
#         print('Please provide a valid number')

#i made the above code and now i realize i can add this to a function after asking chat gpt so i will try to make the function myself now

def getNumbers(prompt):
    while True: 
        try: 
            return float(input(prompt)) 
        except ValueError: 
            print('please provide a valid number')
# the above function will try to define if it a valid number or not
#in case of error it will provide an error and ask the user to try again.

num1 = getNumbers('Please input the number: ')
num2 = getNumbers('Please input the number: ')
num3 = getNumbers('Please input the number: ')

if num1 > num2 and num1 > num3:
    print(f'{num1} is the largest number')
elif num2 > num1 and num2 > num3:
    print(f'{num2} is the largest number')
else:
    print(f'{num3} is the largest number')
# the above if statement is made to make sure we print the value highest. 