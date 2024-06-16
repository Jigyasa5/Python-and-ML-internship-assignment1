# QUE 23) Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input
temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit of temperature (C for Celsius, F for Fahrenheit): ")
if unit.upper() == 'C':
    fahrenheit = (temperature * 9/5) + 32
    print("The temperature temperature°C is equal to ",fahrenheit ,"F")
elif unit.upper() == 'F':
    celsius = (temperature - 32) * 5/9
    print("The temperature {temperature}°F is equal to", celsius ,"C" )
else:
    print("Invalid unit!")