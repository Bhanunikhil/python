num1=list(input())
num2=list(input())
num3=""
for i in range(len(num1)):
    if num1[i]==num2[i]:
        num3= num3+"0"
    else:
        num3=num3+"1"
print(num3)