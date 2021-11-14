import itertools
N = int(input())
A = [list(map(int, input().split())) for i in range(N)]
M = int(input())
XY = set()
for _ in range(M):
    x, y = map(int, input().split())
    XY.add((x-1,y-1))
    XY.add((y-1,x-1))

ath = [i for i in range(N)]

ans = 10**10

for l in itertools.permutations(ath):
    check_comb = set()
    for i in range(N-1):
        check_comb.add((l[i],l[i+1]))
    if 0 < len(check_comb&XY): continue

    t = 0
    for i, k in enumerate(l):
        t += A[k][i]
    ans = min(ans, t)

if ans == 10**10:
    print(-1)
else:
    print(ans)



