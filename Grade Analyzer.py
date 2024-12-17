# Let's ask for input and assign variables to them.
sName = input("Name of the person we're calculating grades for: ")
iTest1 = int(input("Test 1: "))
iTest2 = int(input("Test 2: "))
iTest3 = int(input("Test 3: "))
iTest4 = int(input("Test 4: "))
sDrop_Answer = input("Do you wish to drop the lowest grade? Enter 'Y' or 'N'.: ")

# We'll make sure the grade input is not less than zero.
if iTest1 < 0 or iTest2 < 0 or iTest3 < 0 or iTest4 < 0:
        print("Test score must be greater than zero.")
        raise SystemExit

# Next, we'll make sure they entered either 'Y' or 'N' to drop a grade.
if sDrop_Answer != 'Y' and sDrop_Answer != 'N':
    print("Enter 'Y' or 'N' to drop the lowest grade.")
    raise SystemExit

# Then we'll run calculations based on which test score is the lowest.
if sDrop_Answer == 'Y':
    if iTest1 < iTest2 and iTest1 < iTest3 and iTest1 < iTest4:
        fAverage = (iTest2 + iTest3 + iTest4) / 3
    elif iTest2 < iTest1 and iTest2 < iTest3 and iTest2 < iTest4:
        fAverage = (iTest1 + iTest3 + iTest4) / 3
    elif iTest3 < iTest1 and iTest3 < iTest2 and iTest3 < iTest4:
        fAverage = (iTest1 + iTest2 + iTest4) / 3
    else:
        fAverage = (iTest1 + iTest2 + iTest3) / 3
# This will work as our 'N' input.
else:
    fAverage = (iTest1 + iTest2 + iTest3 + iTest4) / 4

# Now we should assign a letter grade based on the averages:
if fAverage >= 97.0:
    sLetterGrade = 'A+'
elif fAverage >= 94.0:
    sLetterGrade = 'A'
elif fAverage >= 90.0:
    sLetterGrade = 'A-'
elif fAverage >= 87.0:
    sLetterGrade = 'B+'
elif fAverage >= 84.0:
    sLetterGrade = 'B'
elif fAverage >= 80.0:
    sLetterGrade = 'B-'
elif fAverage >= 77.0:
    sLetterGrade = 'C+'
elif fAverage >= 74.0:
    sLetterGrade = 'C'
elif fAverage >= 70.0:
    sLetterGrade = 'C-'
elif fAverage >= 67.0:
    sLetterGrade = 'D+'
elif fAverage >= 64.0:
    sLetterGrade = 'D'
elif fAverage >= 60.0:
    sLetterGrade = 'D-'
else:
    sLetterGrade = 'F'

print(f"{sName}, your test average is {fAverage:.1f}.")
print(f"Your letter grade for the test is {sLetterGrade}")