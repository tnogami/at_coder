N, M, K = map(int, input().split())

# NとMの最小公倍数
def lcm(x, y):
    import math
    return (x * y) // math.gcd(x, y)

A = lcm(N, M)

ok = 10**24
ng = 0

def check(k):
    ct = k // N
    ct += k // M
    ct -= 2*(k // A)
    return ct >= K 
    

while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)