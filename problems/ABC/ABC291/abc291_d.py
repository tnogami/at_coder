MOD = 998244353
N = int(input())
AB = [tuple(map(int,input().split())) for _ in range(N)]

dp = [[0,0] for _ in range(N)]
dp[0][0] = dp[0][1] = 1

for i in range(N-1):
    pre_a, pre_b = AB[i]
    cur_a, cur_b = AB[i+1]
    if pre_a != cur_a:
        dp[i+1][0] += dp[i][0]

    if pre_a != cur_b:
        dp[i+1][1] += dp[i][0]

    if pre_b != cur_a:
        dp[i+1][0] += dp[i][1]

    if pre_b != cur_b:
        dp[i+1][1] += dp[i][1]

    dp[i+1][0] %= MOD
    dp[i+1][1] %= MOD

print(sum(dp[-1])%MOD)