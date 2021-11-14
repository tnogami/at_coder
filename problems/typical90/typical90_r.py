import math
def pos(t):
    global T, L
    y = L/2.0*math.sin(-2*t/T*math.pi)
    z = L/2.0*math.sin(2*t/T*math.pi - math.pi/2.0) + L/2.0
    return y, z

T = float(input())
L, X, Y = map(int, input().split())

Q = int(input())

for _ in range(Q):
    y, z = pos(float(input()))
    d = math.sqrt(X**2+(Y-y)**2+z**2)
    theta = math.asin(z/d)
    print(math.degrees(theta))




