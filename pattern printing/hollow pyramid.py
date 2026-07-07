num = int(input("Enter number of rows: "))

for i in range(num):

    # Spaces
    for j in range(num - i - 1):
        print(" ", end=" ")

    # Stars
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == num - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()