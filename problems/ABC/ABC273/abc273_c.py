from collections import Counter
import bisect
N = int(input())
A = list(map(int,input().split()))
ct = Counter(A)
ans = [0]*N
setA = set(A)
A = list(setA)
A.sort()
M = len(A)

for a in setA:
    idx = bisect.bisect(A, a)
    s = M - idx
    ans[s] += ct[a]

for a in ans:
    print(a)



