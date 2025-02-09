def reverse_string(input_string):
    reversedString = "".join(reversed(input_string))
    return reversedString

print(reverse_string('Hello Work'))


def sum_of_digits(num: int):
    # define the length of the calculcation, but why?
    sumDigits = 0
    numString = str(num)
    lengthNum = len(str(num))
    for i in range(lengthNum):
        sumDigits += int(numString[i])
    return sumDigits
        
print(sum_of_digits(123))

def is_palindrome(string):
    reverseredString = "".join(reversed(string))
    if string == reverseredString:
        return True
    else:
        return False

print(is_palindrome('raceca r'))

def find_fibonacci(n):
    if n <= 0:
        return []  
    
    fib_series = [0, 1]  
    while True:
        next_fib = fib_series[-1] + fib_series[-2]  # Calculate the next Fibonacci number
        if next_fib > n:
            break  # Stop if the next number exceeds n
        fib_series.append(next_fib)

    return fib_series

def calculate_average(numbers: list)-> float:
    if numbers == []:
        return 0
    average = sum(numbers) / len(numbers)    
    return average

list = [5, 10, 15, 20]
calculate_average(list)

def count_occurrences(numbers, target):
    count = 0
    for i in numbers:
        if i == target:
            count += 1
        else:
            pass
    return count

list = [1, 2, 3, 4, 2, 2, 5]
count_occurrences(list, 2)

def find_missing_number(nums):
    # Your code here
    orderedNums = nums.sort()
    print(orderedNums)

find_missing_number([4, 1, 3, 2, 0, 6, 7, 5])