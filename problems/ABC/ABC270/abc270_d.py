N, K = map(int, input().split())
A = list(map(int,input().split()))

dp = [0 for _ in range(N+1)]

for n in range(1, N+1):
    for k in range(K):
        if n < A[k]: break
        dp[n] = max(dp[n], A[k] + n - A[k] - dp[n-A[k]])
print(dp[N])
