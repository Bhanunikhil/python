ans=[]
for _ in range(int(input())):
    a, b = map(int, input().split())
    remainder = a % b
    if remainder == 0:
        ans.append(0)
    else:
        ans.append(b - remainder)
for i in ans:
    print (i)