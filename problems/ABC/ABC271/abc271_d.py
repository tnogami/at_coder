N, S = map(int, input().split())
AB = [tuple(map(int,input().split())) for _ in range(N)]
dp = [[None]*(S+1) for _ in range(N+1)]

for n in range(N):
    a, b = AB[n]
    for i in range(S+1):
        if n == 0 and i == 0:
            if i+a <= S:
                dp[n+1][i+a] = 0
            if i+b <= S:
                dp[n+1][i+b] = 1
        else:
            if dp[n][i] is None: continue

            if i+a <= S:
                dp[n+1][i+a] = 2*dp[n][i]
            if i+b <= S:
                dp[n+1][i+b] = 2*dp[n][i] + 1

if dp[N][S] is None:
    print("No")
else:
    print("Yes")
    ans = []
    b = bin(dp[N][S])[2:]
    b = b.zfill(N)
    for i in b:
        if i == "0":
            ans.append("H")
        else:
            ans.append("T")
    print("".join(ans))


