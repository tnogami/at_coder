N, K = map(int, input().split())
c = [0 for i in range(N+1)]
ans = 0
for i in range(2, N+1):
    if c[i] != 0 : continue
    for k in range(1, N+1):
        j = i * k
        if N < j :break
        c[j] += 1

ans = 0
for i in c:
    if K <= i : ans += 1

print(ans)
