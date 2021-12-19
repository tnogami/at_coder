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

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

N, M = map(int, input().split())
nodes = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    nodes[a-1].append(b-1)

uf = UnionFind(N)
ans = [0]
nodes = nodes[1:]
nodes = nodes[::-1]
g = 0 #グループ数
for i, edges in enumerate(nodes):
    #頂点が増えた分グループを追加
    g += 1
    #繋がるグループ数
    s = set()
    for e in edges:
        s.add(uf.find(e))
    m = len(s)
    for e in edges:
        uf.union(e, N-i-1)
    #現在のグループ数から新規につながった分を引く
    g -= m
    ans.append(g)

ans = ans[::-1]
for a in ans:
    print(a)

