a, b = input().split()
ab = a*int(b)
ba = b*int(a)
ans = [ab,ba]
ans.sort()
print(ans[0])