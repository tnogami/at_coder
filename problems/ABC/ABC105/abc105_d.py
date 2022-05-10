from itertools import accumulate
from collections import defaultdict
N, M = map(int, input().split())
A = list(map(int,input().split()))

A = list(map(lambda x:x%M, A))
A_acc = list(accumulate(A))
ans = 0
d = defaultdict(int)
d[0] = 1

for a in A_acc:
    ans += d[(M-a)%M]
    d[(M-a)%M] += 1

print(ans)
