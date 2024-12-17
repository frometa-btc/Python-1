# Begin with the input.
# I'm using this part to add a conversion (decimal to percentage) so I don't have to do it later.
fPrincipal = float(input("Enter the starting principal: "))
fInterestRate = float(input("Enter the annual interest rate: ")) / 100
fCompound = float(input("How many times per year is the interest compounded?: "))
fLength = float(input("For how many years will the account earn interest?: "))

# Convert and Process below as needed.
fFutureValue = fPrincipal * (1 + fInterestRate / fCompound) ** (fCompound * fLength)

# Print the output below.
print(f"At the end of {fLength} years, you will have ${fFutureValue:,.2f}")