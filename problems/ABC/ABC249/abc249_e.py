N, P = map(int, input().split())
dp = [[0]*4200 for _ in range(3100)]
dp[0][0] = 1

for i in range(N):
    c = 26
    if i != 0:
        c = 25
        for j in range(N+1):
            dp[i][j+1] += dp[i][j]
            dp[i][j+1] %= P

    for j in range(N+1):
        for digit in range(1,5):
            dp[i+digit+1][j+10**(digit-1)] += c*dp[i][j]
            if digit != 4:dp[i+digit+1][j+10**(digit)] -= c*dp[i][j]

ans = 0
for i in range(N):
    ans += dp[i][N]
    ans %= P
print(ans)




