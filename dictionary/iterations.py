dict1={

    "name":"richu", "age":21, "place":"cochin"
}


for i in dict1:#normal iteration through keys
    print(i)


for i in dict1.keys():  #iteration through keys using key() function
    print(i)

for i in dict1.values():  #iteration using value() function
    print(i)


for i in dict1.items():#using item() function
    print(i)