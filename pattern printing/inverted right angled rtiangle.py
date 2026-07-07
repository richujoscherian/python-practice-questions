num=int(input("enter the number of rows"))

for i in range(num):
    for j in range(num,i,-1):
        print("*",end=" ")
    print()
