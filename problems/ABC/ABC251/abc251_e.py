N = int(input())
A = list(map(int,input().split()))

ans = 10**24

#A_1を払う場合
dp = [[10**24]*2 for _ in range(N+1)]
dp[1][0] = A[0]
for i in range(1, N):
    dp[i+1][0] = min(dp[i][0]+A[i], dp[i][1]+A[i])
    dp[i+1][1] = dp[i][0]

ans = min(dp[N])
#A_Nを払う場合
dp = [[10**24]*2 for _ in range(N+1)]
dp[1][0] = A[N-1]
for i in range(1, N):
    dp[i+1][0] = min(dp[i][0]+A[i-1], dp[i][1]+A[i-1])
    dp[i+1][1] = dp[i][0]
ans = min(ans, min(dp[N]))

print(ans)

