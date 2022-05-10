N = int(input())
withdraw = [1]

for i in range(1,7):
    withdraw.append(6**i)
    withdraw.append(9**i)

withdraw.sort()

dp = [10**9]*(N+1)
dp[0] = 0

for i in range(N):
    for d in withdraw:
        if N < i+d : break
        dp[i+d] = min(dp[i]+1, dp[i+d])

print(dp[N])




