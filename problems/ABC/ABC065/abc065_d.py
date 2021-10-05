import copy
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

    def same(self, x, y):
        return self.find(x) == self.find(y)

N = int(input())
xy = []
for i in range(N):
    x, y = map(int, input().split())
    xy.append((i, x, y))
xy.sort(key=lambda x: x[1])
x_sorted = copy.deepcopy(xy)
xy.sort(key=lambda x: x[2])
y_sorted = copy.deepcopy(xy)
edges = []
for i in range(N-1):
    node1x = x_sorted[i][0]
    node2x = x_sorted[i+1][0]
    costx = x_sorted[i+1][1] - x_sorted[i][1]
    edges.append((node1x, node2x, costx))
    node1y = y_sorted[i][0]
    node2y = y_sorted[i+1][0]
    costy = y_sorted[i+1][2] - y_sorted[i][2]
    edges.append((node1y, node2y, costy))

edges.sort(key=lambda x : x[2])
uf = UnionFind(N)
ans = 0
for edge in edges:
    if uf.same(edge[0], edge[1]):continue
    uf.union(edge[0], edge[1])
    ans += edge[2]

print(ans)


