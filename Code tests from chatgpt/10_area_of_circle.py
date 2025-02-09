import math
#imported math to be able to use the math.pi function

def circle_area(radius):
    return math.pi * radius**2
#made the above functioon calculate the radius of the circle. 

while True: 
    try:
        radius = int(input('Input number: '))
        if radius <= 0:
            print("Radius must be greater than zero")
            continue 
        #ensures the radius is greater than zero here. 
        break
    except ValueError:
        print("Please input a valid radius in format of a number")
#validate the input with the above while statement to ensure a valid radius is inputted

result = circle_area(radius)

print(f'The area of a circle = {result:.2f} for a radius of {radius}')