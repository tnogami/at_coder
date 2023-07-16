from collections import deque
N, M = map(int, input().split())
P = list(map(int, input().split()))
nodes = [[] for _ in range(N)]

for i, p in enumerate(P, 1):
    p -= 1
    nodes[p].append(i)

X2Y = {str(n): 0 for n in range(N)}

for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    if y+1 > X2Y[str(x)]:
        X2Y[str(x)] = y+1


dist = [-1]*N  # 距離

dq = deque()

# 始点の設定
dq.append((0, X2Y['0']))
dist[0] = 0

# キューが無くなるまでループ
ans = 0
while dq:
    cur, y = dq.popleft()
    if 0 < y:
        ans += 1

    for next_node in nodes[cur]:
        if dist[next_node] != -1:
            continue
        if y-1 < X2Y[str(next_node)]:
            next_y = X2Y[str(next_node)]
        else:
            next_y = y-1
        dq.append((next_node, next_y))
        dist[next_node] = dist[cur] + 1

print(ans)
