staff={"id":1234,"name":"richu","designation":"softeware engineer","company":"gooogle","salary":5000}
print("id:",staff["id"])
print("name:",staff["name"])
print("designation:",staff["designation"])
print("company:",staff["company"])
print("salary:",staff["salary"])




staff["location"]="kochi"

print(staff["location"])

staff["salary"]=100000
print("---------------------------------------after updation-------------------------------------------")
for key,value in staff.items():
    print(key,":",value)
