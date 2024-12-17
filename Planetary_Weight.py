# Define the name of each planet and assign it a weighted value.
nMERCURY = 0.38
nVENUS = 0.91
nMOON = 0.165
nMARS = 0.38
nJUPITER = 2.34
nSATURN = 0.93
nURANUS = 0.92
nNEPTUNE = 1.12
nPLUTO = 0.066

# Enter prompts for input from the user.
sName = input("Welcome to my weight conversion program! What is your name?: ")
nWeight = float(input(f"Nice to meet you, {sName}! How much do you weigh on Earth?: "))

# Use space below for processing, calculations, and conversions.
nMercuryWeight = nWeight * nMERCURY
nVenusWeight = nWeight * nVENUS
nMoonWeight = nWeight * nMOON
nMarsWeight = nWeight * nMARS
nJupiterWeight = nWeight * nJUPITER
nSaturnWeight = nWeight * nSATURN
nUranusWeight = nWeight * nURANUS
nNeptuneWeight = nWeight * nNEPTUNE
nPlutoWeight = nWeight * nPLUTO

# Enter all print functions here.
print(f"{sName}, here's what your weight would be on all of our Solar System's planets: ")
print(f"Weight on Mercury:   {nMercuryWeight:10.2f}lbs")
print(f"Weight on Venus:     {nVenusWeight:10.2f}lbs")
print(f"Weight on our Moon:  {nMoonWeight:10.2f}lbs")
print(f"Weight on Mars:      {nMarsWeight:10.2f}lbs")
print(f"Weight on Jupiter:   {nJupiterWeight:10.2f}lbs")
print(f"Weight on Saturn:    {nSaturnWeight:10.2f}lbs")
print(f"Weight on Uranus:    {nUranusWeight:10.2f}lbs")
print(f"Weight on Neptune:   {nNeptuneWeight:10.2f}lbs")
print(f"Weight on Pluto:     {nPlutoWeight:10.2f}lbs")