N, P, Q, R, S = map(int, input().split())
A = list(map(int,input().split()))
a1 = A[:P-1]
a2 = A[P-1:Q]
a3 = A[Q:R-1]
a4 = A[R-1:S]
a5 = A[S:]
print(*(a1+a4+a3+a2+a5))