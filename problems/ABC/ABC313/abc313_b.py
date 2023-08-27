N, M = map(int, input().split())
ct = [0]*N
for _ in range(M):
    a, b = map(int, input().split())
    b -= 1
    ct[b] += 1

ans = []
for i, c in enumerate(ct):
    if c == 0:
        ans.append(i+1)

if len(ans) > 1:
    print(-1)
else:
    print(ans[0])
