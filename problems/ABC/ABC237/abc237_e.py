from heapq import heappush, heappop
INF = 10 ** 9
def dijkstra(s): # (始点, ノード数)
    dist = [INF] * N
    hq = [(0, s)] # (distance, node)
    dist[s] = 0
    visited = [False] * N # ノードが確定済みかどうか
    while hq:
        v = heappop(hq)[1] # ノードを pop する
        visited[v] = True
        for to, cost in nodes[v]: # ノード v に隣接しているノードに対して
            if visited[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist


N, M = map(int, input().split())
H = list(map(int,input().split()))
nodes = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    if H[u-1] < H[v-1]:
        nodes[u-1].append((v-1, H[v-1]-H[u-1]))
        nodes[v-1].append((u-1, 0))
    else:
        nodes[v-1].append((u-1, H[u-1]-H[v-1]))
        nodes[u-1].append((v-1, 0))

dist = dijkstra(0)
ans = [0]*N
for i in range(N):
    ans[i] = H[0]-H[i]-dist[i]
print(max(ans))
