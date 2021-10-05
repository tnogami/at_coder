import itertools
N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

for i in range(1, 2*N):
    T[i%N] = min(T[(i-1)%N]+S[(i-1)%N], T[i%N])

for t in T:
    print(t)