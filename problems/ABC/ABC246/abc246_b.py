import math
A, B = map(int, input().split())

C = math.sqrt(A**2+B**2)
print(A/C, B/C)