from collections import deque
import string

H, W = map(int, input().split())
field = [input() for _ in range(H)]
dist = [[-1]*W for _ in range(H)]

worps = [list() for _ in range(26)]
alpha = set(list(string.ascii_lowercase))

for i in range(H):
    for j in range(W):
        c = field[i][j]
        if c == "S":
            start = (i,j)
            continue

        if c == "G":
            goal = (i,j)
            continue

        if c in alpha:
            idx = ord(c)-97
            worps[idx].append((i,j))

#幅優先探索
dx = (0,1,0,-1)
dy = (1,0,-1,0)

#始点の設定
i, j = start
dist[i][j] = 0
dq = deque([(i,j)])

#キューが無くなるまでループ
while dq:
    cur_y, cur_x = dq.popleft()
    field_cur = field[cur_y][cur_x]

    #ワープマスの場合はワープ
    if field_cur.islower():
        for next_y, next_x in worps[ord(field_cur)-97]:
            if dist[next_y][next_x] != -1 : continue #訪問済み
            dist[next_y][next_x] = dist[cur_y][cur_x] + 1
            dq.append((next_y,next_x))

    #上下左右に移動
    for k in range(4):
        next_y, next_x = cur_y+dy[k], cur_x+dx[k]
        if next_x < 0 or W <= next_x or next_y < 0 or H <= next_y : continue #マスの外
        if field[next_y][next_x] == "#" : continue #壁
        if dist[next_y][next_x] != -1 : continue #訪問済み
        dist[next_y][next_x] = dist[cur_y][cur_x] + 1
        dq.append((next_y,next_x))

i, j = goal
print(dist[i][j])
