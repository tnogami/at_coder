#ダイクストラ法
# from heapq import heappush, heappop
# def dijkstra(s, n): # (始点, ノード数)
#     ret = []
#     dist = [10**20] * n
#     hq = [(0, s, -1)] # (distance, node)
#     dist[s] = 0
#     seen = [False] * n # ノードが確定済みかどうか
#     while hq:
#         d, v, idx = heappop(hq) # ノードを pop する
#         if seen[v]: continue
#         if v != 0:
#             ret.append(idx)
#         seen[v] = True
#         for to, cost, idx in nodes[v]: # ノード v に隣接しているノードに対して
#             if seen[to] == False and dist[v] + cost < dist[to]:
#                 dist[to] = dist[v] + cost
#                 heappush(hq, (dist[to], to, idx))
#     return ret

import heapq
def dijkstra(s, n, c_list):
    ret = []
    _list = [float("Inf")]*n
    _list[s] = 0
    hq = [[0,s,0]]
    heapq.heapify(hq)
    while len(hq) > 0:
        _ci, _i, _k = heapq.heappop(hq)
        if _list[_i] < _ci:
            continue
        if len(ret) <= N-2 and _k != 0:
            ret.append(_k)
        for _j,_cj,_k in c_list[_i]:
            if _list[_j] > (_list[_i] + _cj):
                _list[_j] = _list[_i] + _cj
                heapq.heappush(hq, [_list[_j],_j,_k])
    return ret

N, M = map(int, input().split())
nodes = [[] for _ in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    nodes[a-1].append((b-1,c,i+1))
    nodes[b-1].append((a-1,c,i+1))
    
print(*dijkstra(0,N,nodes))