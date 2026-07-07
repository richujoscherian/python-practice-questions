array1=[1,2,3,4,5]
array2=[4,21,87,1,2,1,1]
new_list=[]

for i in array1:
    for j in array2:
        if i==j and i not in new_list:

            new_list.append(i)
print(new_list)

