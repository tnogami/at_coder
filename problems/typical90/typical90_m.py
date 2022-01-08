from heapq import heappush, heappop
INF = 10 ** 9
def dijkstra(s, dist): # (始点, ノード数)
    hq = [(0, s)] # (distance, node)
    seen = [False] * N
    dist[s] = 0
    while hq:
        v = heappop(hq)[1] # ノードを pop する
        seen[v] = True
        for to, cost in nodes[v]: # ノード v に隣接しているノードに対して
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))


N, M = map(int, input().split())
nodes = [[] for _ in range(N)]
dist_to_N = [float(INF) for i in range(N)]
dist_from_1 = [float(INF) for i in range(N)]

for _ in range(M):
   a, b, c = map(int, input().split())
   nodes[a-1].append((b-1, c))
   nodes[b-1].append((a-1, c))

dijkstra(0, dist_from_1)
dijkstra(N-1, dist_to_N)

for i in range(N):
    print(dist_from_1[i] + dist_to_N[i])