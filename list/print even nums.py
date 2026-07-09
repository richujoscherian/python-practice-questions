# array1=[10,15,20,56,59,48]
# ans=[]
#
# for i in array1:
#     if i%2==0:
#         ans.append(i)
#
# print(ans)



array1=[10,15,20,56,59,48,12,21,54,98876,964651536]

for i in array1[:]:
    if i%2!=0:

        array1.remove(i)

print(array1)


