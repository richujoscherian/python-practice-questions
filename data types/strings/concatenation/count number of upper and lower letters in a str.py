str1=str(input("enter the string"))
upper=0
lower=0
for i in str1:
    if i>='A' and i<='Z':
        upper+=1

    if i>='a' and i<='z':
        lower+=1
print(upper,"-upper",lower,"-lower")


#we can also use