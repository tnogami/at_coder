N, X = map(int, input().split())
T = list(map(int, input().split()))
t1 = T[0]

mod = 998244353
dp = [0] * (X + 1)  # ある時刻に音楽がちょうど終わる確率
dp[0] = 1

inv = pow(N, mod - 2, mod)
ans = 0
for i in range(X):
    for k in range(N):
        if k == 0:
            if i + t1 <= X:
                dp[i + t1] += dp[i] * inv
                dp[i + t1] %= mod
            else:
                ans += dp[i] * inv
                ans %= mod
        else:
            if i + T[k] <= X:
                dp[i + T[k]] += dp[i] * inv
                dp[i + T[k]] %= mod
            else:
                continue

print(ans)
