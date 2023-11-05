from bisect import bisect_left
N, M = map(int, input().split())
A = list(map(int, input().split()))

for i in range(1, N+1):
    idx = bisect_left(A, i)
    print(A[idx]-i)
