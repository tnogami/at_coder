S = input()
ans = 0
for i, c in enumerate(S[::-1]):
    ans += (ord(c)-ord('A')+1) * 26**i
print(ans)