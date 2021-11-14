import itertools
import collections

def xytoidx(x, y):
    return 1000*y+x


N = int(input())

field = [0]*(1000*1000+1)

for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())
    for i in range(ly, ry):
        field[xytoidx(lx,i)] += 1
        field[xytoidx(rx,i)] -= 1

ans = list(itertools.accumulate(field))
ct = collections.Counter(ans)

for i in range(N):
    print(ct[i+1])
    