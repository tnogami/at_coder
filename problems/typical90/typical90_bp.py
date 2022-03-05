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

    def members(self, x):
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

N = int(input())
Q = int(input())

uf = UnionFind(N)

N_sum = [-1 for _ in range(N)]
is_ambiguous = []
query1 = []

query_num = 0
for q in range(Q):
    T, X, Y, V = map(int, input().split())
    if T == 0:
        N_sum[X-1] = V
        uf.union(X-1,X)
    else:
        query1.append((T, X, Y, V))
        if uf.same(X-1,Y-1):
            is_ambiguous.append(False)
        else:
            is_ambiguous.append(True)

ans = [1]

a = 1
for i in range(N-1):
    if N_sum[i] == -1:
        ans.append(1)
        a = 1
    else:
        ans.append(N_sum[i]-a)
        a = N_sum[i]-a

for i, q in enumerate(query1):
    if is_ambiguous[i]:
        print("Ambiguous")
    else:
        T, X, Y, V = q
        diff = V - ans[X-1]
        a = ans[Y-1] + diff*(-1)**((X+Y)&1)
        print(a)

