import math
MOD = 998244353
N, K, M = map(int, input().split())
if math.gcd(M,MOD) == 1:
    a = pow(K, N, MOD-1)
    ans = pow(M, a, MOD)
    print(ans)
else:
    print(0)