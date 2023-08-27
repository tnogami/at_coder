import sys

sys.setrecursionlimit(10**9)


def dfs(i):
    visited[i] = True

    for j in nodes[i]:
        if visited[j] == True:
            continue
        dfs(j)

    ans.append(i+1)


N = int(input())
nodes = [[] for i in range(N)]
visited = [-1 for i in range(N)]
ans = []

for i in range(N):
    C = list(map(int, input().split()))
    if C[0] == 0:
        continue

    for j in C[1:]:
        nodes[i].append(j-1)

dfs(0)
print(*ans[:-1])
