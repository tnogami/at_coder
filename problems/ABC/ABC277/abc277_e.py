
from collections import deque
N, M, K = map(int, input().split())

dist = [[-1]*2 for _ in range(N)]

nodes = [{i:[] for i in range(2)} for _ in range(N)]

for _ in range(M):
    u, v, a = map(int, input().split())
    u -= 1
    v -= 1
    nodes[u][a].append(v)
    nodes[v][a].append(u)

S = set(list(map(int,input().split())))
S = set(map(lambda x:x-1, S))

dq = deque()

# 始点の設定
dq.append((0,1))
dist[0][1] = 0
if 0 in S:
    dq.append((0,0))
    dist[0][0] = 0
    

#キューが無くなるまでループ
while dq:
    cur, state = dq.popleft()

    for next_node in nodes[cur][state]:
        if dist[next_node][state] != -1 : continue
        dq.append((next_node, state))
        dist[next_node][state] = dist[cur][state] + 1

        if next_node in S:
            if dist[next_node][(state+1)%2] == -1:
                dq.append((next_node, (state+1)%2))
                dist[next_node][(state+1)%2] = dist[cur][state] + 1

s = min(dist[N-1])
l = max(dist[N-1])

if s < 0:
    print(l)
else:
    print(s)