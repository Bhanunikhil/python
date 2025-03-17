num1 = list(map(int, input().split()))
unique_colors = set(num1)
ans = len(num1) - len(unique_colors) 

print(ans)
