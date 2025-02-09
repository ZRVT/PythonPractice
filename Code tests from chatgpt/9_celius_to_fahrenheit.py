def celsius_to_fahrenheit(celsius):
   return (celsius * 9/5 ) + 32

while True: 
    try:
        celsius = float(input('Fill in celcius temprature: '))
        break
    except ValueError:
            print('Please provide a valid input')
fahrenheit = celsius_to_fahrenheit(celsius)

print(f'The temprature in Fahrenheit = {fahrenheit:.2f}')
print(f'The temprature in celcius = {celsius:.2f}')