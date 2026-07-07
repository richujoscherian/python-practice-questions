num = int(input("Enter number of rows: "))

for i in range(num):

    # Leading spaces
    for j in range(i):
        print(" ", end=" ")

    # Stars
    for j in range(2 * (num - i) - 1):
        if i == 0 or j == 0 or j == 2 * (num - i) - 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()