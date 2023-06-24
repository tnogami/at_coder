N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

dp = [[-10**18,-10**18] for _ in range(N+1)]
dp[0][0] = 0

for n in range(N):
    X, Y = XY[n]
    if X == 0:
        dp[n+1][0] = max(dp[n][0], dp[n][1]+Y, dp[n][0]+Y)
        dp[n+1][1] = dp[n][1]
    else:
        dp[n+1][0] = dp[n][0]
        dp[n+1][1] = max(dp[n][0]+Y, dp[n][1])

print(max(dp[N]))
