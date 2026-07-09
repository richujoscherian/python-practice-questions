person={"id":1234,"name":"Richu","age":22,"place":"kottyam","designation":"software engineer","company":"google","salary":"65lpa","contact_number":546465321,"email":"richu@gmail.com"}
print("______________________________________________person details___________________________________________________________________________________________________________________")
print("id :",person["id"])
print("name :",person["name"])
print("age :",person["age"])
print("place :",person["place"])
print("designation :",person["designation"])
print("company:",person["company"])
print("number:",person["contact_number"])
print("salary:",person["salary"])
print("email:",person["email"])


#updation

person["tel.num"]=4828211957   #adding new key and value
person["place"]="calicut"       #updating value
person.update({"name":"kichu"})#updating using update method
del person["salary"]#using del
person.pop("company")#using pop
print(person)

person.clear()#using clear


print(person)
