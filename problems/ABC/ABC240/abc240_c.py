N, X = map(int, input().split())
dp = [[False]*(X+1) for _ in range(N+1)]
dp[0][0] = True

for n in range(N):
    a, b = map(int, input().split())
    for x in range(X+1):
        if dp[n][x] == False : continue
        for m in [a,b]:
            if X < x+m: continue
            dp[n+1][x+m] = True

if dp[N][X]:
    print("Yes")
else:
    print("No")


