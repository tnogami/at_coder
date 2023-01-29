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

N, M = map(int, input().split())
out_ct = [0]*N
uf = UnionFind(N)
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    out_ct[u] += 1
    out_ct[v] += 1
    uf.union(u,v)

one_ct = 0
flag = True
for ct in out_ct:
    if ct == 1:
        one_ct += 1
    elif ct == 2:
        continue
    else:
        flag = False

if one_ct != 2:flag=False

if uf.group_count() != 1:
    print("No")
elif flag:
    print("Yes")
else:
    print("No")