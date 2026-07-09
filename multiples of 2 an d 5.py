array1=[10,15,20,56,59,48]
ans=[]

for i in array1:
    if i%5==0 and i%2==0:
        ans.append(i)

print(ans)