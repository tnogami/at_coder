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

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members


N, M = map(int, input().split())
uf = UnionFind(N)
edges = [set([]) for _ in range(N)]
for m in range(M):
    u, v = map(int, input().split())
    uf.union(u-1, v-1) #辺を追加
    edges[u-1].add(m)
    edges[v-1].add(m)

for gms in uf.all_group_members().values():
    l = len(gms)
    eg = set()
    for gm in gms:
        eg |= edges[gm]

    if l == len(eg):
        continue
    else:
        print("No")
        break
else:
    print("Yes")