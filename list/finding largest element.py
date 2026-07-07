mylist=[1,54,4,87,95,65]
max=1

for i in mylist:
    if i >max:     #here during every iteration it compares with every element in the list and the max and swap the value if found a greater value
        max=i
print(max)

#
# working:
# 1>54 is false then swap it with max ,
# then 54>4 is true so it continues and the process continues in every iteration
#54>87 is false max=87