import bisect
import array
L, Q = map(int, input().split())

splt = array.array("i", [0, L])

for i in range(Q):
    c, x = map(int, input().split())
    if c == 1:
        idx = bisect.bisect(splt, x)
        splt.insert(idx, x)
    else:
        r_idx = bisect.bisect(splt,x)
        l_idx = r_idx - 1
        print(splt[r_idx]- splt[l_idx])