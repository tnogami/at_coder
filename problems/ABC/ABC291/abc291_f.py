N, M = map(int, input().split())
S = [input() for _ in range(N)]
dp1 = [10**9]*(N+10)
dp2 = [10**9]*(N+10)
dp1[0] = 0
dp2[0] = 0

for n in range(N):
    s = S[n]
    for i in range(M):
        if s[i] == '1':
            dp1[n+i+1] = min(dp1[n+i+1], dp1[n] + 1)

for n in range(N):
    for i in range(M):
        if N < (n+i+2):continue
        c = S[-(n+i+2)][i]
        if c == '1':
            dp2[n+i+1] = min(dp2[n+i+1], dp2[n] + 1)

ans = [10**9]*(N-2)

for n in range(N-2):
    s = S[n]
    for i, c in enumerate(s):
        if i == 0: continue
        if c == '0': continue
        if dp1[n] == -1: continue
        if dp2[N-1-(n+i+1)] == -1: continue
        for k in range(1, i+1):
            ans[n+k-1] = min(ans[n+k-1], dp1[n] + dp2[N-1-(n+i+1)] + 1)

ans = [a if a != 10**9 else -1 for a in ans]

print(*ans)
