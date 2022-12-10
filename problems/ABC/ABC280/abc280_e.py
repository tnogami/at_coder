N, P = map(int, input().split())
MOD = 998244353
dp = [0]*(N+1)
dp[0] = 0
dp[1] = 1
p = (P*pow(100, MOD-2, MOD))%MOD
q = (1-p)%MOD

for n in range(N-1):
    dp[n+2] = p*(dp[n]+1) + q*(dp[n+1]+1)
    dp[n+2] %= MOD

print(dp[N])