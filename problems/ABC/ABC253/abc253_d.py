import math

def lcm(a, b):
    n= a*b // math.gcd(a, b)
    return int(n)

N, A, B = map(int, input().split())
s = N*(N+1)//2
C = lcm(A,B)

na = N // A
sa = na*(2*A+(na-1)*A)//2

nb = N // B
sb = nb*(2*B+(nb-1)*B)//2

nc = N // C
sc = nc*(2*C+(nc-1)*C)//2

print(s-sa-sb+sc)

