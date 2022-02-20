N, S = map(int, input().split())
dp = [[""]*(S+1) for _ in range(N+1)]
dp[0][0] = "I"

for n in range(N):
    a, b = map(int, input().split())
    d = dict()
    d[a] = "A"
    d[b] = "B"
    for s in range(S+1):
        if not dp[n][s] : continue
        for m in [a,b]:
            if S < s + m : continue
            dp[n+1][s+m] = dp[n][s]+d[m]

if dp[N][S]:
    print(dp[N][S][1:])
else:
    print("Impossible")



