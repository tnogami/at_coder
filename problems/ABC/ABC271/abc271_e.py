N, M, K = map(int, input().split())
ABC = [tuple(map(int, input().split())) for _ in range(M)]
E = list(map(int,input().split()))

dp = [10**21]*N
dp[0] = 0

for e in E:
    a, b, c = ABC[e-1]
    a -= 1
    b -= 1
    dp[b] = min(dp[b], dp[a]+c)

if dp[N-1] == 10**21:
    print(-1)
else:
    print(dp[N-1])

 

