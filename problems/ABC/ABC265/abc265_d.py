from itertools import accumulate
from bisect import bisect

N, P, Q, R = map(int, input().split())
A = list(map(int,input().split()))
acc = [0] + list(accumulate(A)) + [10**21]

ans = False
for x in range(N-1):
    target = P + acc[x]
    idx = bisect(acc, target)

    if acc[idx-1] == target:
        y = idx - 1
        target = Q + acc[y]
        idx = bisect(acc, target)

        if acc[idx-1] == target:
            z = idx - 1
            target = R + acc[z]
            idx = bisect(acc, target)

            if acc[idx-1] == target:ans = True

if ans:
    print("Yes")
else:
    print("No")

