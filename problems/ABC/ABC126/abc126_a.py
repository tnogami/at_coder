N, K = map(int, input().split())
S = input()
ans = ""
for i,s in enumerate(S):
    if i+1 == K:
        ans += s.lower()
    else:
        ans += s
print(ans)