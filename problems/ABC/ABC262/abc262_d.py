N = int(input())
A = list(map(int,input().split()))
MOD = 998244353
ans = N
for p in range(2, N+1):
    dp = [[[0]*p for _ in range(p+1)] for _ in range(N+1)]
    dp[0][0][0] = 1

    for n in range(N):
        m = A[n]%p
        for k in range(p+1):
            for j in range(p):
                #toranaitoki
                dp[n+1][k][j] += dp[n][k][j]
                dp[n+1][k][j] %= MOD
                #torutoki
                if k != p:
                    dp[n+1][k+1][(j+m)%p] += dp[n][k][j]
                    dp[n+1][k+1][(j+m)%p] %= MOD

    ans += dp[N][p][0]%MOD

print(ans%MOD)


