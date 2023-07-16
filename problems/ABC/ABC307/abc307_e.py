N, M = map(int, input().split())

MOD = 998244353

dp = [[0]*2 for _ in range(N)]
dp[0][0] = 1

# 0 -> ある数で終わる
# 1 -> ある数で終わらない
for n in range(N-1):
    dp[n+1][0] = dp[n][1]*1
    dp[n+1][0] %= MOD
    dp[n+1][1] = dp[n][0]*(M-1) + dp[n][1]*(M-2)
    dp[n+1][1] %= MOD

ans = M*dp[N-1][1]
ans %= MOD

print(ans)
