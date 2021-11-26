def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

fact = [1, 1]
factinv = [1, 1]
inv = [0, 1] 

N, M, K = map(int,input().split())
p = 998244353

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

ans = 0
for k in range(K+1):
    ans += cmb(N-1, k, p) * M * pow(M-1, N-k-1, p)
    ans %= p
print(ans)