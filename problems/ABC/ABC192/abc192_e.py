input_count = 0

import heapq

def dijkstra(s):
    hq = [(0, s)]
    heapq.heapify(hq) # リストを優先度付きキューに変換
    cost = [10**18] * N # 行ったことのないところはinf
    cost[s] = 0 # 開始地点は0
    while hq:
        c, v = heapq.heappop(hq)
        if c > cost[v]: # コストが現在のコストよりも高ければスルー
            continue
        for to, d, k in nodes[v]:
            if cost[v]%k == 0:
                wait = 0
            else:
                wait = k - cost[v]%k
            tmp = d + wait + cost[v]
            if tmp < cost[to]:
                cost[to] = tmp
                heapq.heappush(hq, (tmp, to))
    return cost

N, M, X, Y = map(int, input().split())
nodes = [[] for _ in range(N)]
for _ in range(M):
    A, B, T, K = map(int, input().split())
    nodes[A-1].append((B-1, T, K))
    nodes[B-1].append((A-1, T, K))
    
cost = dijkstra(X-1)

if cost[Y-1] == 10**18:
    print(-1)
else:
    print(cost[Y-1])
