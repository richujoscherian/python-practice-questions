num = int(input("Enter number of rows: "))
for i in range(num):
    for j in range(i+1):
        if j==i or j==0 or i==num-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()

