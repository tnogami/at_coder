
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

H, W = map(int, input().split())
uf = UnionFind(H*W)
field = [False for i in range(H*W)]

Q = int(input())
for i in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        idx = W*(q[1]-1)+q[2]-1
        field[idx] = True
        check = []
        if H != 1:
            if idx < W:
                check.append(idx+W)
            elif W*(H-1) <= idx:
                check.append(idx-W)
            else:
                check.append(idx+W)
                check.append(idx-W)

        if W != 1:     
            if idx%W == 0:
                check.append(idx+1)
            elif idx%W == W-1:
                check.append(idx-1)
            else:
                check.append(idx+1)
                check.append(idx-1)

        for c in check:
            if field[c] == True: uf.union(idx, c)

    else:
        idx1 = W*(q[1]-1)+q[2]-1
        idx2 = W*(q[3]-1)+q[4]-1
        if field[idx1] == False or field[idx2] == False:
            print("No")
        else:
            if uf.same(idx1, idx2):
                print("Yes")
            else:
                print("No")




