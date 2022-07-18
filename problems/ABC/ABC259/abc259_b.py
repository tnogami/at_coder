import math
A, B, D = map(int, input().split())
D = math.radians(D)
x = math.cos(D)*A - math.sin(D)*B
y = math.sin(D)*A + math.cos(D)*B
print(x,y)