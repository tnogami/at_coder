
import io
import sys
import itertools



# input here
_INPUT = """\
1 1
2 3 4 56 5 6
""" 
sys.stdin = io.StringIO(_INPUT)


# your code here

N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for p in itertools.permutations(range(N), N):
    t = 0
    p = list(p)
    if p[0] != 0 : continue
    p.append(0)
    for i in range(len(p)-1):
        t += T[p[i]][p[i+1]]
    if t == K : ans += 1

print(ans)

