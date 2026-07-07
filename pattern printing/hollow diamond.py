num = int(input("Enter number of rows: "))

# Upper half
for i in range(num):

    for j in range(num - i - 1):
        print(" ", end=" ")

    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Lower half
for i in range(num - 2, -1, -1):

    for j in range(num - i - 1):
        print(" ", end=" ")

    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()