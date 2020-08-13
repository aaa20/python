#step 1
operation = input("Would you like to add/subtract/multiply/divide?").lower()
print("You chose {}.".format(operation))

#step 2
if operation == "subtract" or operation == "divide":
    print("You chose {}".format(operation))
    print("Please keep in mind that the order pf your numbers matter.")

num1 = input("What is the first number?")
num2 = input("What is the second number?")

print("First number: {}".format(num1))
print("Second number: {}".format(num2))

#step3
try:
    num1, num2 = float(num1), float(num2)
    if operation == "add":
        result = num1 + num2
        print("{} + {} = {}".format(num1, num2, result))

    elif operation == "subtract":
        result = num1 - num2
        print("{} - {} = {}".format(num1, num2, result))

    elif operation == "miltiply":
        result = num1 * num2
        print("{} * {} = {}".format(num1, num2, result))

    elif operation == "divide":
        result = num1 / num2
        print("{} / {} = {}".format(num1, num2, result))

    else:
        print("Sorry, but '{}' is not an option.".format(num1, num2, result))
except:
    print("Error: Improper numbers used. Please try again")