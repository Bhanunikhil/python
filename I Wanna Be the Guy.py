n = int(input())
list1=list(map(int,input().split()))[1:]
list2=list(map(int,input().split()))[1:]
list3=list1+list2
for i in range(1,n+1):
    if i not in list3:
        print("Oh, my keyboard!")
        exit()
print("I become the guy.")