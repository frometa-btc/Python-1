# I'm starting with my super-special welcome message here, as I want it to be the first thing users see before any input.
print('''Hello, and welcome to my Temperature Converter Program!
My name is Darwin, and I'll be helping you convert temperature, since apparently Google is not good enough for you.
''')

# Listed variables.
sFahrenheit1 = 'F'
sFahrenheit2 = 'f'
sCelsius1 = 'C'
sCelsius2 = 'c'

# Write input requests below with assigned variables.
fUserTemp = float(input("Please enter a temperature (you can be exact): "))
sUserScale = input("Is the temperature in Fahrenheit (enter 'F') or Celsius (enter 'C')?: ")

# Error code for anything other than requested parameters.
if sUserScale != sFahrenheit1 and sUserScale != sCelsius1 and sUserScale != sFahrenheit2 and sUserScale != sCelsius2:
    print("You must enter an 'F' or a 'C'.")
    raise SystemExit
# Time to do a whole bunch of math.
else:
    # Conversion 1 - Convert Fahrenheit to Celsius.
    if sUserScale == sFahrenheit1 or sUserScale == sFahrenheit2:
        if fUserTemp > 212:
            print("Temp cannot be greater than 212 degrees.")
        else:
            sFahrenheit = (5.0 / 9) * (fUserTemp - 32)
            print(f"The Fahrenheit equivalent is {sFahrenheit:.1f} degrees.")
    # Conversion 2 - Convert Celsius to Fahrenheit.
    elif sUserScale == sCelsius1 or sUserScale == sCelsius2:
        if fUserTemp > 100:
            print("Temp cannot be greater than 100 degrees")
        else:
            sCelsius = ((9.0 / 5.0) * fUserTemp) + 32
            print(f"The Celsius equivalent is {sCelsius:.1f} degrees.")