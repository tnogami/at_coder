from itertools import product

N = int(input())

for A, B, C in product(range(N+1), repeat=3):
    if A + B + C > N:
        continue
    print(A, B, C)