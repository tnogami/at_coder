import math
a, b, c = map(int, input().split())
n = math.gcd(math.gcd(a,b), c)

print((a+b+c)//n - 3)