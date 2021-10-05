def dfs(n, color):
    colors[n] = color

    next_color = 1
    for node in nodes[n]:
        if color[node] != -1: continue
        if next_color == color:
            next_color += 1
        dfs()





N = int(input())
nodes = [[] for i in range(N)]
colors = [-1 for i in range(N)]

for i in range(N-1):
    a, b = map(int, input().split())
    nodes[a-1].append(b-1)
    nodes[b-1].append(a-1)






