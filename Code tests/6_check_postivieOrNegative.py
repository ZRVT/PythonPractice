while True:
    try:
        num = float(input('Please input your number: '))
        break
    except ValueError:
        print("please input a valid number.")        

if num == 0:
    print('Number is zero')
elif num > 0:
    print('Number is positive')
else:
    print('Number is negative')