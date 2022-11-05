import sys
sys.setrecursionlimit(10**9)
def dfs(n, depth):
    ans[n] = depth

    for to in nodes[n]:
        if ans[to] != -1: continue
        dfs(to, depth+1)

N = int(input())
A = list(map(int,input().split()))

nodes = [[] for _ in range(2*N+1)]

for i, a in enumerate(A):
    i += 1
    nodes[a-1].append(2*i-1)
    nodes[a-1].append(2*i)

ans = [-1]*(2*N+1)

dfs(0, 0)

for a in ans:
    print(a)
