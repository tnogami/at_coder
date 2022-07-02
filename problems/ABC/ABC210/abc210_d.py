H, W, C = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
dp = [[10**15]*(W+2) for _ in range(H+2)]

ans = 10**15
for k in range(2):
    if k == 1:
        B = []
        for a in A:
            B.append(a[::-1])
        A = B
        dp = [[10**12]*(W+2) for _ in range(H+2)]

    for j in range(1,W+1):
        for i in range(1,H+1):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], A[i-1][j-1]-C*(i+j))

    for j in range(1,W+1):
        for i in range(1,H+1):
            c = A[i-1][j-1] + C*(i+j)
            ans = min(ans, c + min(dp[i-1][j],dp[i][j-1]))

print(ans)