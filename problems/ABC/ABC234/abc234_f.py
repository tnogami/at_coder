from collections import Counter
MOD = 998244353

def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = 998244353
N = 10 ** 5  # N は必要分だけ用意する
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
 
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

S = input()
ct = Counter(S)
letters = list(ct.values())

length = len(S)
kinds = len(ct)

dp = [[0]*(length+1) for _ in range(kinds+1)]
for i in range(kinds+1):
    dp[i][0] = 1

for n in range(kinds):
    for i in range(length+1):
        if dp[n][i] == 0: continue
        for k in range(0,letters[n]+1):
            if i == 0 and k == 0:continue
            dp[n+1][i+k] += dp[n][i]*cmb(i+k,k,MOD)
            dp[n+1][i+k] %= MOD

print((sum(dp[kinds][1:]))%MOD)



