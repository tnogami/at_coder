N, K, D = map(int, input().split())
A = list(map(int,input().split()))

dp = [[[-1]*D for _ in range(K+1)] for _ in range(N+1)]
dp[0][0][0] = 0

for n in range(N):
    a = A[n]
    for k in range(K):
        for m in range(D):
            if dp[n][k][m] == -1:continue
            mod = a%D
            dp[n+1][k+1][(m+mod)%D] = max(dp[n+1][k+1][(m+mod)%D], dp[n][k][m]+a)
            dp[n+1][k][m] = max(dp[n+1][k][m], dp[n][k][m])

ans = -1
for n in range(N+1):
    ans = max(ans, dp[n][K][0])
print(ans)

