from heapq import heappush, heappop
INF = 10 ** 9
def dijkstra(s, n, nodes): # (始点, ノード数)
    dist = [INF] * n
    hq = [(0, s)] # (distance, node)
    dist[s] = 0
    seen = [False] * n # ノードが確定済みかどうか
    while hq:
        v = heappop(hq)[1] # ノードを pop する
        seen[v] = True
        for to, cost in nodes[v]: # ノード v に隣接しているノードに対して
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist

N, M, T = map(int, input().split())
A = list(map(int, input().split()))

to_nodes = [[] for i in range(N)]
from_nodes = [[] for i in range(N)]

for i in range(M):
    a, b, c = map(int,input().split())
    to_nodes[a-1].append((b-1, c))
    from_nodes[b-1].append((a-1, c))

to_dist = dijkstra(0, N, to_nodes)
from_dist = dijkstra(0, N, from_nodes)

ans = 0
for i in range(N):
    rest_time = T - (to_dist[i]+from_dist[i])
    if rest_time <= 0: continue
    ans = max(ans, rest_time*A[i])
print(ans)

