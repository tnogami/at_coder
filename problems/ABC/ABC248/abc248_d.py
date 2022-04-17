from collections import defaultdict
import bisect
N = int(input())
A = list(map(int,input().split()))
Q = int(input())
d_list = defaultdict(list)
for i, a in enumerate(A):
    d_list[a].append(i)

for _ in range(Q):
    L, R, X = map(int, input().split())
    L -= 1
    R -= 1
    l_idx = bisect.bisect_left(d_list[X], L)
    r_idx = bisect.bisect(d_list[X], R)
    print(r_idx-l_idx)


