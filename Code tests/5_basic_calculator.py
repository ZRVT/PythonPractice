# while True: 
#     num1 = float(input('Enter first number: '))
#     if num1 == float: 
#         break
#     else:
#         print('Please provide a valid number')
#when i tried to run the above code it didn't work as it is a number
#for integers or floats i need to do it with the Try / Except logic.  

while True: 
    try:
        num1 = float(input('Enter first number: '))
        break
    except ValueError:
        print('invalid input. Please enter a valid number') 

while True:
    operator = input('Enter operator: (+, -, *,/) ')
    if operator in ('+','-','*','/'):
        break
    else:
        print('Invalid operator please try again')

while True: 
    try:
        num2 = float(input('Enter second number: '))
        #used an if statement below here to make no division is done on 0
        if operator == '/' and num2 == 0:
            print('Division not possible by 0')
        else:
            break
    except ValueError:
        print('Please input a valid number')


if operator == '-':
    result = num1 - num2
elif operator == '+':
    result = num1 + num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
# else:
#     print('Invalid operator')
#removed the else statement in the if function above here. 

print(f'The result of {num1} {operator} {num2} = {result}!')