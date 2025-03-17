count=0
for i in range(int(input())):
	x=input().split()
	if x.count("1")>=2: count=count+1
print(count)