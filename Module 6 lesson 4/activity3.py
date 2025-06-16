num = int(input("Enter a number: "))

if num > 1:
    for n in range(2, num):
        if num % n == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
