from functools import reduce
import math

N, X, Y = map(int, input().split())
BS = [list(map(int, input().split())) for _ in range(N-1)]
S = set(map(lambda x: x[0], BS))


def lcm(a, b):
    n = a*b // math.gcd(a, b)
    return int(n)

# リストを受け取って最小公倍数を返す関数


def my_lcm(nums):
    return reduce(lcm, nums)


pattern = my_lcm(S)

take_time = []
for s in range(pattern):
    t = s
    for bs in BS:
        p, tt = bs
        if t % p == 0:
            t += tt
        else:
            wait_t = p - (t % p)
            t += tt + wait_t
    take_time.append(t-s)

Q = int(input())
for _ in range(Q):
    q = int(input())
    start = (q + X) % pattern
    t = take_time[start]
    print(q+t+X+Y)
