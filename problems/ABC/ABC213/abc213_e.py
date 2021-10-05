import collections

H, W = map(int, input().split())
field = [input() for i in range(H)]

dist = [[10**9 for i in range(W)] for j in range(H)] #距離
seen = [[False for i in range(W)] for j in range(H)]
dq = collections.deque()


dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)
exdx = (2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, -1, -1, -1, -1, -1, -2, -2, -2)
exdy = (1, 0, -1, 2, 1, 0, -1, -2, 2, 1, -1, -2, 2, 1, 0, -1, -2, 1, 0, -1)

# 始点の設定
dq.append((0,0))
dist[0][0] = 0
seen[0][0] = True

#キューが無くなるまでループ
while dq:
    cur_y, cur_x = dq.pop()
    seen[cur_y][cur_x] = True

    #ブロックを壊さずに移動
    for k in range(4): 
        next_y, next_x = cur_y+dy[k], cur_x+dx[k]
        if next_x < 0 or W <= next_x or next_y < 0 or H <= next_y : continue #マスの外
        if seen[next_y][next_x] : continue #訪問済み
        if field[next_y][next_x] == "#" : continue #壁
        if dist[next_y][next_x] <= dist[cur_y][cur_x] : continue
        dist[next_y][next_x] = dist[cur_y][cur_x]
        dq.append((next_y,next_x))

    #ブロック破壊移動
    for k in range(20):
        next_y, next_x = cur_y+exdy[k], cur_x+exdx[k]
        if next_x < 0 or W <= next_x or next_y < 0 or H <= next_y : continue #マスの外
        if seen[next_y][next_x] : continue #訪問済み
        if dist[next_y][next_x] <= dist[cur_y][cur_x] + 1 : continue
        dist[next_y][next_x] = dist[cur_y][cur_x] + 1
        dq.appendleft((next_y,next_x))
        
for i in range(H):
    print(dist[i])
print(dist[H-1][W-1])
