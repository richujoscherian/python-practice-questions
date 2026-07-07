rows=int(input("enter the number"))

for i in range(num):

    for j in range(i):
        print(" ",end=" ")

    for k in range(2*(num-i)-1):
        print("*",end=" ")


    print()
