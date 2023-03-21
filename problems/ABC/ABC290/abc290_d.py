import math
T = int(input())

for _ in range(T):
    N, D, K = map(int, input().split())
    g = math.gcd(N,D)
    n = N // g
    ct = (K-1) // n
    idx = K % n
    print(ct + (((idx-1) * D))%N)

