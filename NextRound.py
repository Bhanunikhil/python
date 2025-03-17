n,k=map(int,input().split())
count=0
a=list(map(int,input().split()))
for j in range(0,len(a)):
	if a[j]>=a[k-1] and a[j]>0: count=count+1
print(count)