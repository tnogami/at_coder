from itertools import accumulate
N, Q = map(int, input().split())
A = list(map(int,input().split()))
B = list(accumulate(A))
C = list(accumulate(B))
D = list(accumulate(C))

print(A,B,C,D)

A[1] = 0

B = list(accumulate(A))
C = list(accumulate(B))
D = list(accumulate(C))

print(A,B,C,D)
