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


from itertools import combinations

uf = UnionFind(1000)

def isSame(a,b):
    next_a = set([(a[0]-1,a[1]-1), (a[0]-1,a[1]), (a[0],a[1]-1), (a[0],a[1]+1), (a[0]+1,a[1]), (a[0]+1,a[1]+1)])
    if b in next_a:
        return True
    return False

N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]

for i,j in combinations(range(N), 2):
    if isSame(XY[i], XY[j]):
        uf.union(i,j)

print(uf.group_count())

    

