MOD = 998244353
N, M, K = map(int, input().split())
dp = [[0]*(K+1) for _ in range(N+1)]
for k in range(K+1):
    dp[0][k] = 1

for i in range(N):
    for k in range(K+1):
        for m in range(1,M+1):
            if K < k + m:break
            dp[i+1][k+m] += dp[i][k]
            dp[i+1][k+m] %= MOD

# print(dp[N])
print((dp[N][-1])%MOD)

