from itertools import accumulate
from bisect import bisect

N = int(input())
A = list(map(int, input().split()))
B = A[:]
B.sort()

acc = [0] + list(accumulate(B))

ans = []
for a in A:
    idx = bisect(B, a)
    ans.append(acc[-1]-acc[idx])

print(*ans)