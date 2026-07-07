str1=str(input("enter the string"))
words=0
in_word=False
for i in str1:
    if i!=" " and in_word==False:
        words+=1
        in_word=True
    if i==" ":
        in_word=False
print(words)


# #with using split build in functio0ns
# str1=str(input("enter the str"))
# x=str1.split()
# print(len(x))


#using strip and split build in functions
# str1 = "  i  am    richu".strip()
# words = str1.split()
#
# count = 0
# for i in words:
#     count += 1
#
# print(count)






