# num=int(input("enter the number"))
# temp=num
#
# sum=0
# length = len(str(num))
# while num>0:
#
#     for i in range(length,0,-1):
#         digit=num%10
#         sum+=digit**i
#         num=num//10
#     if sum==temp:
#         print("yes")
#
#     else:
#         print("no")



num=int(input("enter the number"))
temp=num
sum=0
length=len(str(num))
while num>0:
     digit=num%10
     sum+=digit**length
     num=num//10
     length-=1
if sum==temp:
     print("diserium ")
else:
    print("not a diserium")
