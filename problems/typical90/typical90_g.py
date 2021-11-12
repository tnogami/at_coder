import bisect
N = int(input())
A = list(map(int,input().split()))
A.sort()
Q = int(input())

for i in range(Q):
    B = int(input())
    idx = bisect.bisect(A,B)
    if idx == N:
        print(B-A[-1])
    elif idx == 0:
        print(A[0]-B)
    else:
        print(min(B-A[idx-1], A[idx]-B))

