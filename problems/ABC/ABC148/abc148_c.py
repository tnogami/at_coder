import math
# 2数を受け取って最小公倍数を返す関数
def lcm(a, b):
    n= a*b // math.gcd(a, b)
    return int(n)
A, B = map(int, input().split())
print(lcm(A,B))