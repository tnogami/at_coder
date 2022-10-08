N = int(input())
P = list(map(int,input().split()))


dp = [[False]*10010 for _ in range(N+1)]
dp[0][0] = True

for n in range(N):
    for i in range(10010):
        if dp[n][i] == False:continue
        dp[n+1][i] = True
        dp[n+1][i+P[n]] = True

print(dp[N].count(True))
