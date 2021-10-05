#深さ優先探索(グラフ)
from heapq import heappush, heappop
INF = 10 ** 9
def dijkstra(s): # (始点, ノード数)
    hq = [(0, s)] # (distance, node)
    dist = [INF] * N
    dist[s] = 0
    seen = [False] * N # ノードが確定済みかどうか
    while hq:
        v = heappop(hq)[1] # ノードを pop する
        seen[v] = True
        for to, cost in nodes[v]: # ノード v に隣接しているノードに対して
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist

N, M = map(int, input().split())
nodes = [[] for i in range(N)]
dist = [[] for j in range(N)]
ans = [[] for i in range(N)]

for i in range(M):
    a,b,c =  map(int,input().split())
    nodes[a-1].append((b-1, c))
    if a == b: ans[a-1].append(c)

for k in range(N):
    dist[k] = dijkstra(k)

for i in range(N):
    for j in range(N):
        if i == j: continue
        d = dist[i][j]+dist[j][i]
        ans[i].append(d)

for i in range(N):
    out = min(ans[i])
    if INF <= out:
        print(-1)
    else:
        print(out)
