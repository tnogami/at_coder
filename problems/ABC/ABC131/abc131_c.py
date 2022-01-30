import math 

def lcm(a, b):
    n= a*b // math.gcd(a, b)
    return int(n)

A, B, C, D = map(int, input().split())
bbyc = B//C
bbyd = B//D
abyc = (A-1)//C
abyd = (A-1)//D
bbycd = B//lcm(C,D)
abycd = (A-1)//lcm(C,D)
print(B - bbyc - bbyd + bbycd - (A-1 - abyc - abyd + abycd))
