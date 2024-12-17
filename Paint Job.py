# Quick Introduction
print("Welcome to Darwin's Paint Job Cost Estimator!")
print("*********************************************")

import math

# Function to check for acceptable input.
def getFloatInput(sPrompt):
    while True:
        try:
            fInput = float(input(sPrompt))
            if fInput > 0:
                return fInput
            else:
                print("Input must be greater than zero.")
        except ValueError:
            print("Input must be a number. Try again.")

# Function to calculate the total cost of labor.
def getLaborHours(fLaborHours, fLaborCharge):
    return fLaborHours * fLaborCharge

# Function to calculate total paint cost.
def getPaintCost(iAmountofPaint, fPaintPrice):
    return iAmountofPaint * fPaintPrice

# Function to get the tax value.
def getSalesTax(sState):
    # For accepting lower and upper case letters:
    sState = sState.lower()

    if sState == "ct" or sState == "vt":
        return 0.06
    elif sState == "ma":
        return 0.0625
    elif sState == "me":
        return 0.085
    elif sState == "ri":
        return 0.07
    else:
        return 0.0

# Function to calculate total costs and print to screen.
def showCostEstimate(fPaintCost: float, fLaborCost: float, fSalesTax: float, fTotalCost: float, sFileName: str):
    sOutput = (
        f"Paint Cost: ${fPaintCost:.2f}\n"
        f"Labor Cost: ${fLaborCost:.2f}\n"
        f"Sales Tax: ${fSalesTax:.2f}\n"
        f"Total Cost: ${fTotalCost:.2f}\n"
    )
    print("\nCost Estimate:")
    print("-----------------------------")
    print(sOutput)
    with open(sFileName, "w") as file:
        file.write(sOutput)
    print(f"File: {sFileName} was successfully created.")

def getGallonsOfPaint(fSquareFeet, fFeetPerGallon):
    iAmountOfPaint = math.ceil(fSquareFeet / fFeetPerGallon)
    return iAmountOfPaint

def main():
    # Ask for input
    fSquareFeet = getFloatInput("\nEnter wall space in square feet: ")
    fPaintPrice = getFloatInput("Enter paint price per gallon: $")
    fFeetPerGallon = getFloatInput("How many feet per gallon?: ")
    fLaborHours = getFloatInput("How many hours of labor per gallon?: ")
    fLaborCharge = getFloatInput("Cost of labor per hour: $")
    sState = input("Enter the state of this job: ")
    sName = input("Enter the client's last name: ")

    # Need to define the file name
    sFileName = f"{sName}_PaintJobOutput.txt"

    # Do the math
    iAmountOfPaint = getGallonsOfPaint(fSquareFeet, fFeetPerGallon)
    fTotalLaborHours = iAmountOfPaint * fLaborHours
    fTotalLaborCost = getLaborHours(fTotalLaborHours, fLaborCharge)
    fTotalPaintCost = getPaintCost(iAmountOfPaint, fPaintPrice)
    fTaxRate = getSalesTax(sState)
    fSalesTax = (fTotalLaborCost + fTotalPaintCost) * fTaxRate
    fTotalCost = fTotalLaborCost + fTotalPaintCost + fSalesTax

    # Output to the screen
    print("\nResult:")
    print("-----------------------------")
    print(f"Gallons of paint required: {iAmountOfPaint}")
    print(f"Total hours of labor required: {fTotalLaborHours}")
    showCostEstimate(fTotalPaintCost, fTotalLaborCost, fSalesTax, fTotalCost, sFileName)

main()