lower=int(input("enter the lower limit"))
upper=int(input("enter the upper limit"))

for i in range(lower,upper+1,+1):
    temp = i
    sum = 0
    length = len(str(i))
    while i>0:



        digit=i%10
        sum+=digit**length
        i=i//10

    if sum==temp:
        print(temp)



