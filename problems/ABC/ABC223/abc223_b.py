s = input()
ans = []
for _ in range(len(s)+1):
    s = s[1:] + s[0]
    ans.append(s)

ans.sort()

print(ans[0])
print(ans[-1])