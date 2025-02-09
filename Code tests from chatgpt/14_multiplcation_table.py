#in this function we are making a multiplication table that outputs for each multiplication a seperate line item.
def multiplication_table(number,multi_range):
    for i in range(1, multi_range + 1):
        result = number * i
        print(f'{number} * {i} = {result}')

#In this function we are making multiplication table that outputs the data in a single row. 
def multiplication_table_horizontal(number, multi_range):
    results = []  
    for i in range(1, multi_range + 1):
        results.append(f'{number} x {i} = {number * i}')  
    print(", ".join(results))

#this function outputs if the user wants the multiplication in a single or multiple rows. 
def multi_normal_horizizontal(multi_format_normal):
    if multi_format_normal == True:
        multiplication_table(number,multi_range)
    elif multi_format_normal == False:
        multiplication_table_horizontal(number, multi_range)

#with this section i am validation the number we will use for the multiplication. 
while True:
    try:
        number = int(input('Please input a valid number: '))
        break
    except ValueError:
        print('Please input a valid integer')

#with this while statement i am trying to define the range and verify it is a proper integer used for the multiplicationt table. 
while True:
    try:
        multi_range =  int(input('Please input a valid range: '))
        break
    except:
        print('Please input a valid range.')

#With this while statement i want to validate a true / false statement and validate it is a true/false
while True:
    try:
        user_input = input('Require normal format or horizontal format: ').strip().lower()
        if user_input in ['true', 'false']:
            multi_format_normal = user_input == 'true'  # Convert to True or False
            break
        else:
            print("Please input True or False")
        
        print(f'The multiplication result of {number} with range {multi_range} is the following:')
        break
    except:
        print("Please input True or False")

#return the finalized result of the user input. 
multi_normal_horizizontal(multi_format_normal)