# num=int(input("enter the number"))
# temp=num
# number=""
#
# while num>0:
#     digit=num%10
#     number=number + str(digit)
#     num=num//10
#
# if number==str(temp):
#     print(temp,"is palindrome")




num=int(input("enter the number"))
temp=num
rev_str=0
while num>0:
    digit=num%10
    rev_str=rev_str*10+digit
    num=num//10
if temp==rev_str:
    print("palindrome")
else:
    print("no")



