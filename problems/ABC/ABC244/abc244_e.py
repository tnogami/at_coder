MOD = 998244353

N, M, K, S, T, X = map(int, input().split())

nodes = [[] for _ in range(N)]

dp = [[[0 for _ in range(2)] for _ in range(N)] for _ in range(K+1)]
dp[0][S-1][0] = 1

for _ in range(M):
    U, V = map(int, input().split())
    nodes[U-1].append(V-1)
    nodes[V-1].append(U-1)

for k in range(K):
    for n in range(N):
        for i in range(2):
            if dp[k][n][i] == 0: continue
            for to in nodes[n]:
                if n == X-1:
                    dp[k+1][to][(i+1)%2] += dp[k][n][i]
                    dp[k+1][to][(i+1)%2] %= MOD
                else:
                    dp[k+1][to][i] += dp[k][n][i]
                    dp[k+1][to][i] %= MOD

print(dp[K][T-1][0])


