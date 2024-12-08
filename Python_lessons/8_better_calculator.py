num1 = float(input("Enter a number: "))
operator = input("Enter a operator: ")
num2 = float(input("Enter a number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "*":
    print(num1 * num2)
else:
    print("Invalid operator")