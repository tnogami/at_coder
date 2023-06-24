from collections import deque
N = int(input())
nodes = [set() for _ in range(N)]

for _ in range(N-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1

    nodes[u].add(v)
    nodes[v].add(u)

for i in range(N):
    if len(nodes[i]) == 1:
        start = i
        break


dist = [-1 for i in range(N)] #距離

dq = deque()

# 始点の設定
dq.append(start)
dist[start] = 0

#キューが無くなるまでループ
while dq:
    cur = dq.popleft()
    
    for next_node in nodes[cur]:
        if dist[next_node] != -1 : continue
        dq.append(next_node)
        dist[next_node] = dist[cur] + 1

ans = []

for i in range(N):
    if dist[i]%3 == 1:
        ans.append(len(nodes[i]))

ans.sort()
print(*ans)