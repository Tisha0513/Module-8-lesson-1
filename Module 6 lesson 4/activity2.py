rows = int(input("Enter the number of rows: "))

for t in range(2, rows + 1):
    for u in range(t):
        print("*", end= " ")
        print()