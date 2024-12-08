while True: 
    name:str = input ("Enter your name: ")
    if name.isalpha():
        break
    else: print("Please enter a valid name")


while True: 
    age:int = input("Enter your age: ")
    if age.isnumeric():
        break
    else: print("Please enter a valid age")


print(f"Hello, {name}. You are {age} years old.")