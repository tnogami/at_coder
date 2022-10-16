N, M = map(int, input().split())
X = list(map(int,input().split()))
d = dict()
for _ in range(M):
    c, y = map(int, input().split())
    d[c] = y

dp = [[-1]*(N+1) for _ in range(N+1)]
dp[0][0] = 0

for n in range(N):
    for k in range(N):
        if dp[n][k] == -1:break
        if k+1 in d:
            bonus = d[k+1]
        else:
            bonus = 0
        #表が出る
        dp[n+1][k+1] = max(dp[n+1][k+1], dp[n][k]+X[n]+bonus)

        #裏が出る
        dp[n+1][0] = max(dp[n+1][0], dp[n][k])

print(max(dp[N]))



