

from collections import deque
N1, N2, M = map(int, input().split())

nodes = [[] for _ in range(N1+N2)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    nodes[a].append(b)
    nodes[b].append(a)


dist = [-1 for i in range(N1+N2)]  # 距離


dq = deque()
# 始点の設定
dq.append(0)
dq.append(N1+N2-1)
dist[0] = 0
dist[N1+N2-1] = 0

# キューが無くなるまでループ
while dq:
    cur = dq.popleft()

    for next_node in nodes[cur]:
        if dist[next_node] != -1:
            continue
        dq.append(next_node)
        dist[next_node] = dist[cur] + 1

print(max(dist[:N1])+max(dist[N1:])+1)
