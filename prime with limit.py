
lower=10
upper=30

for i in range(lower, upper+1):
        for num in range(2, i):
            if i % num == 0:
                break
        else:
            print(i)