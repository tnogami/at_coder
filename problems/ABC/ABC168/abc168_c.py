import math

A, B, H, M = map(int, input().split())
degH = 360 * float(H)/12.0 + 30 * float(M)/60.0
degM = 360 * float(M)/60.0

diff = abs(degH - degM)
if diff > 180: diff = 360 - diff

c2 = A**2 + B**2 -2*A*B*math.cos(math.pi*diff/180.0)

print(math.sqrt(c2))
