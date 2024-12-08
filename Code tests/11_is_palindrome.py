def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

while True: 
    string = input('Input your palindrom: ')
    if string == str:
        break
    else:
        print("please proivide a string")
result = is_palindrome(string)

print(f'The input your provided is a palindrum: {result}')