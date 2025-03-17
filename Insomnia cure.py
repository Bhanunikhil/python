k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

ans=set()
for attack in (k,l,m,n):
    for i in range(attack, (d+1), attack):
        ans.add(i)
print(len(ans))
    