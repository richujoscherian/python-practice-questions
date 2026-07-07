num=int(input("enter the number"))
x=str(num)
sum=0
for i in x:
    sum+=int(i)
print(sum)

if num%sum==0:
    print("its a harshad number")
