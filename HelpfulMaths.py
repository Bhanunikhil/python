arr=list(map(int,input().split()))
arr.sort()
for i in range(len(arr)-1):
    print(str(arr[i]) + '+')
x=len(arr)-1
print(arr[x])