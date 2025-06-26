# get user input
choiceFrom = input("Input the tempurature type to convert from (F (Fahrenheit), C (Celsius), K (Kelvin)): ")
choiceTo = input("Input the tempurature type convert to (F (Fahrenheit), C (Celsius), K (Kelvin)): ")
choiceNum = int(input("Input the tempurature amount: "))

# conversion
if choiceFrom == "F":

    if choiceTo == "C":
        result = (choiceNum - 32) / 1.8
    elif choiceTo == "K":
        result = (choiceNum - 459.67) / 1.8
    else:
        print(f"{choiceTo} is not a valid input")

elif choiceFrom == "C":

    if choiceTo == "F":
        result = choiceNum / 1.8 + 32
    elif choiceTo == "K":
        result = choiceNum + 273.15
    else:
        print(f"{choiceTo} is not a valid input")

elif choiceFrom == "K":

    if choiceTo == "F":
        result = choiceNum * 1.8 + 459.67
    elif choiceTo == "C":
        result = choiceNum - 273.15
    else:
        print(f"{choiceTo} is not a valid input")

else:
    print(f"{choiceFrom} is not a valid input")

# print result
print(f"{choiceNum}{choiceFrom} = {result}{choiceTo}")


