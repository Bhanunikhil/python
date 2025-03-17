arr=input()
lst=sorted([int(num) for num in arr.split('+')])
print("+".join(map(str,lst)))