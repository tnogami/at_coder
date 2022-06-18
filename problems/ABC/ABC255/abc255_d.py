from bisect import bisect
from itertools import accumulate
N, Q = map(int, input().split())
A = list(map(int,input().split()))
A.append(0)
A.append(10**18)
A.sort()

acc = list(accumulate(A))
for _ in range(Q):
    x = int(input())
    idx = bisect(A,x)
    plus = x*(idx-1) - acc[idx-1]
    minus = acc[N] - acc[idx-1] - x*(N-idx+1)
    print(plus+minus)
