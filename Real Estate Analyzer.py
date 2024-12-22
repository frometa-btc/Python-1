# Start with Real Estate Analyzer Special Intro

print("BDJ Real Estate Sales Analyzer Tool")
print("-----------------------------------")

# Create functions needed for the program.
# 1. Function to check for valid input, return a float.
def getFloatInput(sPrompt):
    while True:
        try:
            fSalePrice = float(input(sPrompt))
            if fSalePrice <= 0:
                print("Entry must be a positive number greater than zero. Try again.")
                continue
            return fSalePrice
        except ValueError:
            print("Not a valid entry. Please use a number.")

# 2. Function that calculates the median value.
def getMedian(iMedian):
    iCount = len(iMedian)
    if iCount % 2 == 1:
        return iMedian[iCount // 2]
    else:
        iMidValue1 = iCount // 2
        iMidValue2 = iMidValue1 - 1
        return (iMedian[iMidValue1] + iMedian[iMidValue2]) / 2

# 3. Classic Main function.
def main():
    fValueCollection = []

    # Asking for input via while loop and appending to list.
    while True:
        fSalePrice = getFloatInput("Please enter the property value.: $")
        fValueCollection.append(fSalePrice)

        # Adding nested while loop for additional values.
        while True:
            fNewInput = input("Enter another property value? (Y/N): ").strip().lower()
            if fNewInput in ('y', 'n'):
                break
            print('Invalid. Please enter "Y" for yes, or "N" for no.')

        if fNewInput == 'n':
            break

    # Using sort to organize entries.
    fValueCollection.sort()

    # Calculations.
    fTotal = sum(fValueCollection)
    fMinimum = fValueCollection[0]
    fMaximum = fValueCollection[-1]
    fAverage = fTotal / len(fValueCollection)
    fMedian = getMedian(fValueCollection)
    fCommission = fTotal * 0.03

    # Output.
    print("\nSales Data Analysis:")
    print("----------------------")
    print("Property Values:")
    for fSalePrice in fValueCollection:
        print(f"User Input: ${fSalePrice:,.2f}")
    print("-------------------------------------------")
    print(f"Minimum: .................${fMinimum:,.2f}")
    print(f"Maximum: .................${fMaximum:,.2f}")
    print(f"Total: ...................${fTotal:,.2f}")
    print(f"Average: .................${fAverage:,.2f}")
    print(f"Median: ..................${fMedian:,.2f}")
    print(f"Commission: ..............${fCommission:,.2f}")

if __name__ == "__main__":
    main()