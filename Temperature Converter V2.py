# I'm starting with my super-special welcome message here, as I want it to be the first thing users see before any input.
print('''Hello, and welcome to my Temperature Converter Program!
My name is Darwin, and I'm here to convert temperature, since apparently Google is not good enough for you.
''')

# Ask for input and assign it a variable.
fUserTemp = float(input("Please enter a temperature (you can be exact): "))
sUserScale = input("Is the temperature in Fahrenheit (enter 'F') or Celsius (enter 'C')?: ")

# Fahrenheit to Celsius conversion.
if sUserScale == 'F' or sUserScale == 'f':
    if fUserTemp > 212:
        print("Temp cannot be greater than 212 degrees.")
    else:
        sCelsius = (5.0 / 9) * (fUserTemp - 32)
        print(f"The Celsius equivalent is {sCelsius:.1f} degrees.")
# Celsius to Fahrenheit conversion.
elif sUserScale == 'C' or sUserScale == 'c':
    if fUserTemp > 100:
        print("Temp cannot be greater than 100 degrees")
    else:
        sFahrenheit = ((9.0 / 5.0) * fUserTemp) + 32
        print(f"The Fahrenheit equivalent is {sFahrenheit:.1f} degrees.")
else:
    print("You must enter an 'F' or a 'C'.")
    raise SystemExit