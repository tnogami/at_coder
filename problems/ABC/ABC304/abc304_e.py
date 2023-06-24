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

for _ in range(M):
    u, v = map(int, input().split())
    uf.union(u-1, v-1)

K = int(input())
is_ok = True
ng_list = set()
for _ in range(K):
    x, y = map(int, input().split())
    if uf.find(x-1) == uf.find(y-1):
        is_ok = False
        break
    else:
        a = uf.find(x-1)
        b = uf.find(y-1)
        if a > b:
            a, b = b, a
        ng_list.add((a,b))

Q = int(input())
for _ in range(Q):
    p, q = map(int, input().split())
    a = uf.find(p-1)
    b = uf.find(q-1)
    if a > b:
        a, b = b, a
    if is_ok and (a, b) not in ng_list:
        print("Yes")
    else:
        print("No")



