import sys

sys.setrecursionlimit(10**9)


def dfs(i, x, y):
    visited[i] = True
    pos[i] = [x, y]

    for to, diff_x, diff_y in nodes[i]:
        if visited[to] == True:
            continue
        dfs(to, x + diff_x, y + diff_y)


N, M = map(int, input().split())
nodes = [[] for _ in range(N)]
visited = [-1 for i in range(N)]
pos = [[0, 0] for _ in range(N)]

for _ in range(M):
    a, b, x, y = map(int, input().split())
    nodes[a - 1].append((b - 1, x, y))
    nodes[b - 1].append((a - 1, -x, -y))

dfs(0, 0, 0)

for i in range(N):
    if visited[i] == -1:
        print("undecidable")
    else:
        print(pos[i][0], pos[i][1])
