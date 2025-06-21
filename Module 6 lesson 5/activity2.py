def fact(t):
    if t == 1:
        return t
    else:
        return t * fact(t-1)

num = int(input("Enter a number: "))

if num < 0:
    print("Sorry! Factorial doesnt exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print(f"the factorial of {num} is", fact(num))