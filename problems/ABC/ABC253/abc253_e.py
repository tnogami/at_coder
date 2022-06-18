from itertools import accumulate

MOD = 998244353

N, M, K = map(int, input().split())

if K == 0:
    print(pow(M,N,MOD))
else:

    dp = [[0]*(M+10) for _ in range(N+1)]

    for m in range(1,M+1):
        dp[1][m] = 1

    for n in range(1,N):
        
        for i in range(M+1):
            if 1 <= i - K:
                dp[n+1][1] += dp[n][i]%MOD
                dp[n+1][i-K+1] -= dp[n][i]%MOD

            if i + K <= M:
                dp[n+1][i+K] += dp[n][i]%MOD
                dp[n+1][M+1] -= dp[n][i]%MOD

        dp[n+1] = list(accumulate(dp[n+1]))
        dp[n+1] = list(map(lambda x : x%MOD, dp[n+1]))

    print(sum(dp[N])%MOD)
