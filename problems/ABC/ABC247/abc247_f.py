import sys
from collections import defaultdict
MOD = 998244353
sys.setrecursionlimit(10**9)

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

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]


def Fib(n):
    global memo
    if n in memo:
        return memo[n]
    else:
        memo[n] = (Fib(n-1) + Fib(n-2))%MOD
        return memo[n]
        
N = int(input())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))
uf = UnionFind(N)

for i in range(N):
    uf.union(P[i]-1,Q[i]-1)

memo = {1:1, 2:3}
Fib(max([uf.size(i) for i in uf.roots()])+1)

ans = 1
for i in uf.roots():
    s = uf.size(i)
    ans *= memo[s]
    ans %= MOD

print(ans)