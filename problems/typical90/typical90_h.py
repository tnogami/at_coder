import copy
MOD = 10**9 + 7
N = int(input())
S = input()

atcoder = "atcoder"

dp = [[0 for i in range(8)] for j in range(N+1)]
for i in range(N+1):
    dp[i][0] = 1

for i,s in enumerate(S):
    if not s in atcoder:
        dp[i+1] = copy.copy(dp[i])
    else:
        dp[i+1] = copy.copy(dp[i])
        idx = atcoder.index(s)
        dp[i+1][idx+1] += dp[i][idx]
        dp[i+1][idx+1] %= MOD

print(dp[N][-1])
