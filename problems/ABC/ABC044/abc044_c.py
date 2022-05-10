N, A = map(int, input().split())
X = list(map(int,input().split()))

X = list(map(lambda x:x-A, X))

dp = [[0]*10000 for _ in range(N+1)]

zero_idx = 5000

dp[0][zero_idx] = 1

for n in range(N):
    for i in range(10000):
        if dp[n][i] == 0 : continue
        dp[n+1][i] += dp[n][i]
        dp[n+1][i+X[n]] += dp[n][i]

print(dp[N][zero_idx]-1)


