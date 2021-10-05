import bisect

N = int(input())
A = list(map(int,input().split()))
A.sort()
amax = max(A)
t = -(-amax//2)

idx = bisect.bisect(A, t)

a = A[idx]
b = A[idx-1]

if abs(t-a) < abs(t-b):
    print(amax, a)
else:
    print(amax, b)