from collections import Counter
import itertools
N, K = map(int, input().split())
A = list(map(int,input().split()))
Acc = list(itertools.accumulate([0] + A))

ct = Counter()
ans = 0

for a in Acc:
    c = a - K
    ans += ct[c]
    ct[a] += 1

print(ans)