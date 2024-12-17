# Intro
print("\nWelcome to Darwin's Compound Interest Calculator!")
print("___________________________________________________")

# Create a function for number validators
def get_valid_number(sPrompt):
    while True:
        try:
            fValue = float(input(sPrompt))
            if fValue < 0:
                print("The value cannot be negative. Please try again.")
                continue
            return fValue
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Create a function to calculate monthly balances over time
def compound_interest_calculator():
    fDeposit = float(get_valid_number("Enter the initial deposit amount: "))
    fInterestRatePercentage = float(get_valid_number("Enter the interest rate: "))
    iMonths = int(get_valid_number("Enter the number of months: "))
    fGoal = float(get_valid_number("What is your savings goal?: "))

    # Convert percentage to decimal
    fInterestRateDecimal = fInterestRatePercentage / 100
    fMonthlyInterestRate = fInterestRateDecimal / 12

    print("\nMonthly Account Balances:")
    print("----------------------------")
    fCurrentBalance = fDeposit
    iCurrentMonth = 1

    while iCurrentMonth <= iMonths:
        fMonthlyInterest = fCurrentBalance * fMonthlyInterestRate
        fCurrentBalance += fMonthlyInterest
        print(f"Month {iCurrentMonth}: ${fCurrentBalance:,.2f}")
        iCurrentMonth += 1

    if fGoal > 0:
        fCurrentBalance = fDeposit
        iMonthsToGoal = 0

        while fCurrentBalance < fGoal:
            fMonthlyInterest = fCurrentBalance * fMonthlyInterestRate
            fCurrentBalance += fMonthlyInterest
            iMonthsToGoal += 1

        print(f"\nIt will take {iMonthsToGoal:,} months to reach your goal of ${fGoal:,.2f}.")
    else:
        print(f"\nNo goal was set, so only the accumulated balances were displayed.")

compound_interest_calculator()