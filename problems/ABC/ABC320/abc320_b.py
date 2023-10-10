s = list(input())

ans = -1
for i in range(len(s) - 1):
    for j in range(i, len(s)):
        if s[i:j] == s[i:j][::-1]:
            ans = max(ans, j - i)

print(ans)
