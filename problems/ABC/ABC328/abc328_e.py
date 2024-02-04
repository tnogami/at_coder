from itertools import combinations


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


N, M, K = map(int, input().split())
edges = []

for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append((u-1, v-1, w))

ans = 10**20
for comb in combinations(range(M), N-1):
    uf = UnionFind(N)
    cost = 0
    for edge_idx in comb:
        u, v, w = edges[edge_idx]
        uf.union(u, v)
        cost += w

    if uf.size(0) == N:
        ans = min(ans, cost%K)

print(ans)