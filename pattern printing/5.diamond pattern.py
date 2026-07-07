num=int(input("enter the number of rows"))

for i in range((num//2) +1):
    for j in range((num//2)+1,i+1,-1):
        print(" ",end=" ")

    for k in range((2*i)+1):
        print("*",end=" ")
    print()
for l in range(num//2):
    for m in range(l+1):
        print(" ",end=" ")

    for n in range(l,(num//2),+1):
        print("*",end=" ")
    for o in range(l+1,num//2):
        print("*", end=" ")
    print()


