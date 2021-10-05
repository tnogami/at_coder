N = int(input())
X, Y = map(int, input().split())

lunchbox = [tuple(map(int, input().split())) for i in range(N)]

INF = 1000
dp = [[[INF for k in range(Y+1)] for j in range(X+1)] for i in range(N+1)]
for i in range(N+1):
    dp[i][0][0] = 0

for i, box in enumerate(lunchbox):
    for x in range(X+1):
        for y in range(Y+1):
            if dp[i][x][y] == INF : continue
            if X < x + box[0]:
                dx = X
            else:
                dx = x + box[0]
            if Y < y + box[1]:
                dy = Y
            else:
                dy = y + box[1]
            dp[i+1][dx][dy] = min(dp[i][x][y] + 1, dp[i+1][dx][dy])
            dp[i+1][x][y] = min(dp[i][x][y], dp[i+1][x][y])

if dp[N][X][Y] == INF:
    print(-1)
else:
    print(dp[N][X][Y])
