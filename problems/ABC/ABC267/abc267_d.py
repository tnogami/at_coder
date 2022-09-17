INF = -5*10**21
N, M = map(int, input().split())
A = list(map(int,input().split()))
dp = [[INF]*(M+10) for _ in range(N+1)]
dp[0][0] = 0

for n in range(N):
    for i in range(M+1):
        if dp[n][i] == INF: continue
        dp[n+1][i] = max(dp[n+1][i], dp[n][i])
        dp[n+1][i+1] = max(dp[n+1][i+1], dp[n][i]+A[n]*(i+1))

print(dp[N][M])

