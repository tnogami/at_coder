mod = 998244353
A, B, C, D, E, F = map(int, input().split())

A %= mod
B %= mod
C %= mod
D %= mod
E %= mod
F %= mod

print((A*B*C-D*E*F)%mod)
