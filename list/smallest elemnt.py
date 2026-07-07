mylist=[45,1,54,4,87,95,65]

smallest=mylist[0]

for i in mylist:
    if i<smallest:
        smallest=i

print(smallest)