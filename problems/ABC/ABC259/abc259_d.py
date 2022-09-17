from collections import defaultdict
def f(i,j):
    ax, ay, ar = XYR[i]
    bx, by, br = XYR[j]
    d = (ax-bx)**2 + (ay-by)**2
    L = (ar+br)**2
    l = (ar-br)**2
    if l <= d <= L:
        return True
    else:
        return False

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

from itertools import combinations
N = int(input())
sx, sy, tx, ty = map(int, input().split())

XYR = [tuple(map(int, input().split())) for _ in range(N)]
XYR.append((sx,sy,0))
XYR.append((tx,ty,0))

uf = UnionFind(N+2)

for i,j in combinations(range(N+2), 2):
    if f(i,j):
        uf.union(i,j)

if uf.same(N,N+1):
    print("Yes")
else:
    print("No")


