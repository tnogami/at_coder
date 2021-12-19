
from collections import defaultdict

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


N, M = map(int, input().split())
neib = [set([]) for i in range(N)]
uf = UnionFind(N)
for _ in range(M):
    A, B = map(int, input().split())
    neib[A-1].add(B-1)
    neib[B-1].add(A-1)
    if 2 < len(neib[A-1]) or 2 < len(neib[B-1]):
        print("No")
        break
    if uf.same(A-1, B-1):
        print("No")
        break
    uf.union(A-1, B-1)
else:
    print("Yes")
