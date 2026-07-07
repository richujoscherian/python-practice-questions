num=int(input("enter the number"))
temp=num
length=len(str(num))
sum=0

while num>0:
    digit=num%10
    sum+=digit**length
    num=num//10
if sum==temp:
    print("it is an armstrong num")
else:
    print("not an armstrong")



