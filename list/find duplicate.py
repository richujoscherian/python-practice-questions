mylist = [45, 1, 54, 1, 4, 87, 4, 95, 65 , 1,4]
duplicates=[]
for i in range(len(mylist)):
    for j in range(i+1,len(mylist)):
        if mylist[j] == mylist[i] and mylist[j] not in duplicates:
            duplicates.append(mylist[i])


print(duplicates)








