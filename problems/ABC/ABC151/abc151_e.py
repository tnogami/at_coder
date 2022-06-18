import bisect

def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = 10 ** 9 + 7
N = 10 ** 6  # N は必要分だけ用意する
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
 
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

N, K = map(int, input().split())
A = list(map(int,input().split()))
A.sort()
d = dict()
setA = set(A)
ans = 0
for a in setA:
    #aが最大値となる場合の数を求める
    idx1 = bisect.bisect_left(A,a)#aより小さいものの数
    idx2 = bisect.bisect_right(A,a)#a以下のものの数
    if K <= idx2:
        ans += a*(cmb(idx2, K, p) - cmb(idx1, K, p))%p
        ans %= p
    
    #aが最小値となる場合の数
    idx3 = N - idx2#aより大きいものの数
    idx4 = N - idx1#a以上のものの数
    if K <= idx4:
        ans -= a*(cmb(idx4, K, p) - cmb(idx3, K, p))%p
        ans %= p

print(ans)