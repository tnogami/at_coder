MOD = 998244353
N, M, K = map(int, input().split())
broken = [[i] for i in range(N)]
for i in range(M):
    u, v = map(int, input().split())
    broken[u-1].append(v-1)
    broken[v-1].append(u-1)

dp = [[0 for i in range(N)] for j in range(K+1)]
dp[0][0] = 1

for k in range(K):
    s = sum(dp[k])
    for n in range(N):
        dp[k+1][n] += s
        dp[k+1][n] %= MOD
        for i in broken[n]:
            dp[k+1][n] -= dp[k][i]
            dp[k+1][n] %= MOD

print(dp[K][0])