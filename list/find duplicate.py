mylist = [45, 1, 54, 1, 4, 87, 4, 95, 65]

for i in range(len(mylist)):
    for j in range(i+1,len(mylist)):
        if mylist[j] == mylist[i]:
            print(mylist[j])





