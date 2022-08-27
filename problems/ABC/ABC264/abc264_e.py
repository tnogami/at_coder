
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

    def members(self, x): #結構遅い
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

N, M, E = map(int, input().split())

uf = UnionFind(N+1)

edges = [tuple(map(lambda x:min(N, int(x)-1), input().split())) for _ in range(E)]

Q = int(input())
downed = [int(input())-1 for _ in range(Q)]
downed_set = set(downed)
score = 0

for i, edge in enumerate(edges):
    if i in downed_set: continue
    u, v = edge
    uf.union(u,v)
    
ans = [uf.size(N)-1]

for idx in downed[::-1]:
    edge = edges[idx]
    u, v = edge
    uf.union(u,v)
    ans.append(uf.size(N)-1)

ans.pop()
for a in ans[::-1]:
    print(a)

