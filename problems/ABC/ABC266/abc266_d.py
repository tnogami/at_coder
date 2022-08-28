N = int(input())
sunukes = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[-1]*5 for _ in range(N+1)]
dp[0][0] = 0

cur_time = 0
for n in range(N):
    time, pos, weight = sunukes[n]
    for i in range(5):
        if dp[n][i] == -1: continue
        t_diff = time - cur_time
        for k in range(max(i-t_diff,0), min(i+t_diff, 4)):
            if k == pos :
                dp[n+1][k] = max(dp[n][i]+weight, dp[n+1][k])
            else:
                dp[n+1][k] = max(dp[n][i], dp[n+1][k])

print(max(dp[N]))