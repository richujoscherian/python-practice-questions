num=int(input("enter the number of rows"))

for i in range(num):

    for k in range(i):
        print(" ",end=" ")
    for j in range((num*2)-1,2*i,-1):
        print("*",end=" ")

    print()
