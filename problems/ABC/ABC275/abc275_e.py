mod = 998244353

def inv(n):
    return pow(n, mod-2, mod)

N, M, K = map(int, input().split())

dp = [[0]*(N+1) for _ in range(K+1)]
dp[0][0] = 1

inv_m = inv(M)

for k in range(K):
    for n in range(N):
        for m in range(1, M+1):
            next_pos = n + m
            if N < next_pos:
                over = next_pos - N
                next_pos = N - over
            dp[k+1][next_pos] += dp[k][n]*inv_m
            dp[k+1][next_pos] %= mod

ans = 0
for d in dp:
    ans += d[N]
    ans %= mod

print(ans)