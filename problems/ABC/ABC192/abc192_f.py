import sys

N, X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

ans = 10**19
for n in range(1,N+1):
    target_mod = X%n
    dp = [[[-1]*n for j in range(n+1)] for i in range(N+1)]
    dp[0][0][0] = 0
    for i in range(N):
        for j in range(n):
            for k in range(n):
                if dp[i][j][k] == -1:continue
                next_mod = (k + A[i])%n
                dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j][k])
                dp[i+1][j+1][next_mod] = max(dp[i+1][j+1][next_mod], dp[i][j][k]+A[i])

    tmp = max([d[n][target_mod] for d in dp])
    if tmp == -1: continue
    ans = min(ans, (X-tmp)//n)

print(ans)