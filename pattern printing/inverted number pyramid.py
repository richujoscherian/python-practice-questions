num = int(input("Enter number of rows: "))

for i in range(num, 0, -1):

    for j in range(num - i):
        print(" ", end=" ")

    for j in range(1, i + 1):
        print(j, end=" ")

    for j in range(i - 1, 0, -1):
        print(j, end=" ")

    print()