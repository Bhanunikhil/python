n = int(input())
if(n>=26):
    string = input().lower()
    string1=set(string)
    ans = len(string1)
    if (ans<26) or any(num.isnumeric() for num in string):
        print ("NO")
    else:
        print ("YES")
else:
    print("NO")