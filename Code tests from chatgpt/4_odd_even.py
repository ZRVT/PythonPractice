number = int(input("Enter a number: "))
#define it as an integer as otherwise will give an error
remainder = number % 2
print(f"The remainder when {number} is divided by 2 is {remainder}")

if remainder == 0:
    print("The number is even")
else:
    print("The number is odd")
