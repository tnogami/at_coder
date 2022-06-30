def alpha2num(s:str):
    return ord(s) - ord("A")

MOD = 998244353

N = int(input())
S = input()


dp = [[[0]*10 for _ in range(2**10)] for _ in range(N+1)]

for s in range(N):
    num_alpha = alpha2num(S[s])

    for n in range(2**10):
        for k in range(10):
            dp[s+1][n][k] += dp[s][n][k]
            dp[s+1][n][k] %= MOD
            if n == 0:
                dp[s+1][n|(1<<num_alpha)][num_alpha] = 1
                continue
            if (n>>num_alpha)&1 == 1 and k == num_alpha:
                dp[s+1][n][k] += dp[s][n][k]
                dp[s+1][n][k] %= MOD
            elif (n>>num_alpha)&1 == 0:
                dp[s+1][n|(1<<num_alpha)][num_alpha] += dp[s][n][k]
                dp[s+1][n|(1<<num_alpha)][num_alpha] %= MOD

ans = 0
for d in dp[N]:
    ans += sum(d)
    ans %= MOD
print(ans)







