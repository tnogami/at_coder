from heapq import heappop, heappush

def dijkstra(s, n):  # (始点, ノード数)
    dist = [10**21] * n
    hq = [(0, s)]  # (distance, node)
    dist[s] = 0
    seen = [False] * n  # ノードが確定済みかどうか
    while hq:
        cost, v = heappop(hq)  # ノードを pop する
        if seen[v]:
            continue
        seen[v] = True
        if dist[v] < cost:
            continue
        for to, cost in adj[v]:  # ノード v に隣接しているノードに対して
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist

N = int(input())
adj = [[] for _ in range(N)]
for n in range(N-1):
    a, b, x = map(int, input().split())
    adj[n].append((x-1, b))
    adj[n].append((n+1, a))

ans = dijkstra(0, N)

print(ans[-1])
