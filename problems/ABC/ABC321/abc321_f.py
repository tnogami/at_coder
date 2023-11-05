Q, K = map(int, input().split())

queries = [input().split() for _ in range(Q)]
mod = 998244353


dp = [0]*(K+1)
dp[0] = 1

for i in range(Q):
    num = int(queries[i][1])

    if queries[i][0] == '+':
        for k in range(K, num-1, -1):
            dp[k] += dp[k-num]
            dp[k] %= mod
    else:
        for k in range(num, K+1):
            dp[k] -= dp[k-num]
            dp[k] %= mod

    print(dp)

    print(dp[K])
