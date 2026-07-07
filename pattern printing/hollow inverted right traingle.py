num = int(input("Enter number of rows: "))

for i in range(num):
    for j in range(num - i):
        if i == 0 or j == 0 or j == num - i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
