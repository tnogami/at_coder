S = input()
N = len(S)
MOD = 998244353
# i文字目までみて、開いたかっこの数がある時の場合の数
dp = [[0] * (N + 1) for _ in range(N + 1)]

dp[0][0] = 1

for i in range(N):
    s = S[i]
    for j in range(N // 2 + 2):
        if dp[i][j] == 0:
            continue

        if s == ")":
            if j == 0:
                continue
            dp[i + 1][j - 1] += dp[i][j]
        elif s == "(":
            dp[i + 1][j + 1] += dp[i][j]
        else:
            dp[i + 1][j + 1] += dp[i][j]
            if j != 0:
                dp[i + 1][j - 1] += dp[i][j]

        dp[i][j] %= MOD

print(dp[N][0] % MOD)
