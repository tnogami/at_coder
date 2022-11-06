from collections import deque
H, W = map(int, input().split())
field = [input() for _ in range(H)]
visited = [[False]*W for _ in range(H)]

dx = (0,1,0,-1)
dy = (1,0,-1,0)

ss = False
for h in range(H):
    for w in range(W):
        if field[h][w] == "S":
            _start = (h, w)
            ss = True
        if ss:break
    if ss:break

starts = []
for k in range(4):
    next_y, next_x = _start[0]+dy[k], _start[1]+dx[k]
    if next_x < 0 or W <= next_x or next_y < 0 or H <= next_y : continue #マスの外
    if field[next_y][next_x] == "#" : continue #壁
    starts.append((next_y, next_x))


flag = False
for start in starts:

    dist = [[-1]*W for j in range(H)] #距離
    dq = deque()

    # 始点の設定
    dq.append(start)
    dist[start[0]][start[1]] = 0

    #キューが無くなるまでループ
    while dq:
        cur_y, cur_x = dq.popleft()

        for k in range(4):
            next_y, next_x = cur_y+dy[k], cur_x+dx[k]
            if next_x < 0 or W <= next_x or next_y < 0 or H <= next_y : continue #マスの外
            if field[next_y][next_x] == "#" or field[next_y][next_x] == "S" : continue #壁
            if dist[next_y][next_x] != -1 : continue #訪問済み
            dist[next_y][next_x] = dist[cur_y][cur_x] + 1
            dq.append((next_y,next_x))

    for start in starts:
        if 2 <= dist[start[0]][start[1]]:
            flag = True
    if flag: break

if flag:
    print("Yes")
else:
    print("No")
