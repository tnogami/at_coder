from collections import deque


def check_attention(h, w, direction):
    start = (h, w)
    while True:
        h, w = h + direction[0], w + direction[1]
        if h < 0 or H <= h or w < 0 or W <= w:
            return
        if field[h][w] == "#" or field[h][w] == ">" or field[h][w] == "<" or field[h][w] == "^" or field[h][w] == "v":
            return
        if field[h][w] == ".":
            attentions[h][w] = True


H, W = map(int, input().split())
field = [list(input()) for _ in range(H)]

attentions = [[False]*W for _ in range(H)]
start = None
goal = None

for h in range(H):
    for w in range(W):
        if field[h][w] == "S":
            start = (h, w)
        if field[h][w] == "G":
            goal = (h, w)
        if field[h][w] == ">":
            check_attention(h, w, (0, 1))
        if field[h][w] == "<":
            check_attention(h, w, (0, -1))
        if field[h][w] == "^":
            check_attention(h, w, (-1, 0))
        if field[h][w] == "v":
            check_attention(h, w, (1, 0))

Nx, Ny = W, H
dist = [[-1 for i in range(Nx)] for j in range(Ny)]  # 距離
dq = deque()
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

# 始点の設定
dq.append(start)
dist[start[0]][start[1]] = 0

# キューが無くなるまでループ
while dq:
    cur_y, cur_x = dq.popleft()

    for k in range(4):
        next_y, next_x = cur_y+dy[k], cur_x+dx[k]
        if next_x < 0 or Nx <= next_x or next_y < 0 or Ny <= next_y:
            continue  # マスの外
        if field[next_y][next_x] == "#" or attentions[next_y][next_x] or field[next_y][next_x] == ">" or field[next_y][next_x] == "<" or field[next_y][next_x] == "^" or field[next_y][next_x] == "v":
            continue  # 壁
        if dist[next_y][next_x] != -1:
            continue  # 訪問済み
        dist[next_y][next_x] = dist[cur_y][cur_x] + 1
        dq.append((next_y, next_x))

print(dist[goal[0]][goal[1]])
