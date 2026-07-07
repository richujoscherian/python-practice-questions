num = int(input("Enter the number: "))

if num <= 1:
    print("Neither Prime nor Composite")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Composite")
            break
    else:
        print("Prime")