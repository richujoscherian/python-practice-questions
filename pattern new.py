num=int(input("enter the number"))
for i in range(1,num+1):
    for j in range(num+1,i,-1):
        print((num+1)-i,end=" ")
    print()

# num=int(input("enter the number"))
# for i in range(rows,0,-1):
#     for j in range(i):
#         print(i,end=" ")
#     print()
