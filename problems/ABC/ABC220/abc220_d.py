MOD = 998244353
N = int(input())
A = list(map(int,input().split()))

dp = [[0 for i in range(10)] for j in range(N)]
dp[0][A[0]] = 1

for i in range(N-1):
    for j in range(10):
        if dp[i][j] == 0: continue
        next_a = A[i+1]
        dp[i+1][(next_a+j)%10] += dp[i][j]
        dp[i+1][(next_a+j)%10] %= MOD

        dp[i+1][(next_a*j)%10] += dp[i][j]
        dp[i+1][(next_a*j)%10] %= MOD

for i in range(10):
    print(dp[N-1][i])



