# number = 1
# number_high = 100

# while number <= number_high:
#     if number % 3 == 0 and number % 5 == 0:
#         print('FizzBuzz')
#     elif number % 3 == 0:
#         print('Fizz')
#     elif number % 5 == 0:
#         print('Buzz')
#     else:
#         print(number)
#     number += 1 

#i did the first solution as above now let me try to do it as function with the for loop again. 

def fizzbuz():
    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
            print('Fizzbuzz')
        elif num % 5 == 0:
            print('Buzz')
        elif num % 3 == 0:
            print('Fizz')
        else: 
            print(num)

fizzbuz()