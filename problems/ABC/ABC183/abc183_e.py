MOD = 10**9 + 7
H, W = map(int, input().split())
field = [input() for _ in range(H)]

dp = [[0]*(W+1) for _ in range(H+1)]
dpu = [[0]*(W+1) for _ in range(H+1)]
dpl = [[0]*(W+1) for _ in range(H+1)]
dpul = [[0]*(W+1) for _ in range(H+1)]

dp[1][1] = 1

for i in range(1,H+1):
    for j in range(1,W+1):
        dp[i][j] += dpu[i-1][j]
        dp[i][j] += dpl[i][j-1]
        dp[i][j] += dpul[i-1][j-1]

        dpu[i][j] = dpu[i-1][j] + dp[i][j]
        dpl[i][j] = dpl[i][j-1] + dp[i][j]
        dpul[i][j] = dpul[i-1][j-1] + dp[i][j]

        dp[i][j] %= MOD
        dpu[i][j] %= MOD
        dpl[i][j] %= MOD
        dpul[i][j] %= MOD

        if field[i-1][j-1] == "#":
            dp[i][j] = 0
            dpu[i][j] = 0
            dpl[i][j] = 0
            dpul[i][j] = 0

print(dp[H][W])


