from itertools import accumulate
from bisect import bisect_left

N, M, P = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

acc = list(accumulate([0]+B))

ans = 0
for a in A:
    idx = bisect_left(B, P - a)
    ans += (M - idx) * P
    ans += a * idx + acc[idx]

print(ans)
