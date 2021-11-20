from heapq import heappush, heappop
INF = 10 ** 12

#移動コストcを引数にして、ゴールまでの最短距離をダイクストラ法で求める。
def dijkstra(c):
    dist = [[INF]*W for i in range(H)]
    seen = [[False]*W for i in range(H)]
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    hq = [(0, (sx, sy))] # (distance, node)
    dist[sy][sx] = 0
    while hq:
        _sx, _sy = heappop(hq)[1] # ノードを pop する
        seen[_sy][_sx] = True
        for k in range(4):
            new_sx = _sx + dx[k]
            new_sy = _sy + dy[k]
            if new_sx < 0 or W <= new_sx or new_sy < 0 or H <= new_sy: continue
            if field[new_sy][new_sx] == "#":
                cost = c
            else:
                cost = 1
            if seen[new_sy][new_sx] == False and dist[_sy][_sx] + cost < dist[new_sy][new_sx]:
                dist[new_sy][new_sx] = dist[_sy][_sx] + cost
                heappush(hq, (dist[new_sy][new_sx], (new_sx, new_sy)))
    return dist[gy][gx]

#入力
H, W, T = map(int, input().split())
field = [input() for i in range(H)]

#スタートとゴールの座標の確認
for i in range(H):
    for j in range(W):
        if field[i][j] == "S": sx,sy = j,i
        if field[i][j] == "G": gx,gy = j,i

ok = 0
ng = 10**12

#二分探索
while 1 < abs(ok - ng):
    mid = (ok + ng)//2
    if dijkstra(mid) <= T:
        ok = mid
    else:
        ng = mid

print(ok)

