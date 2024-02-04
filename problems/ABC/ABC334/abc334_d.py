from itertools import accumulate
from bisect import bisect_left, bisect_right
N, Q = map(int, input().split())
R = list(map(int, input().split()))

R.sort()

acc_R = [0] + list(accumulate(R))

for i in range(Q):
    X = int(input())
    idx = bisect_right(acc_R, X)
    print(idx-1)


