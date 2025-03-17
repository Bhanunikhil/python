string=input()
str1 = list(map(str, string))
index=0
str2=""
str1[index]=str1[index].upper()
for i in range(len(str1)):
    str2=str2+str1[i]
print(str2)