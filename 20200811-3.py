try:
    ans = float(input("Type a number to add: "))
    print("100 + {} = {}".format(ans, 100 + ans))
except:
    print("You did not put in a valid number!")

print("The program did not break!")