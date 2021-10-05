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

abc = [tuple(map(int, input().split())) for i in range(M)]

abc.sort(key=lambda x:x[2])

uf = UnionFind(N)

ans = 0

for a,b,c in abc:
    a -= 1
    b -= 1
    if c <= 0:
        uf.union(a,b)
    else:
        if uf.same(a,b):
            ans += c
        else:
            uf.union(a,b)

print(ans)




