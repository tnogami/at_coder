from collections import deque

H, W = map(int, input().split())
field = [input() for _ in range(H)]

dist = [[-1 for i in range(W)] for j in range(H)]  # 距離
dq = deque()
# 8方向
dx = (0, 1, 0, -1, 1, 1, -1, -1)
dy = (1, 0, -1, 0, 1, -1, 1, -1)

ct = 0
for i in range(H):
    for j in range(W):
        if field[i][j] == ".":
            continue
        # 訪問済み
        if dist[i][j] != -1:
            continue

        # 始点の設定
        dq.append((i, j))
        dist[i][j] = 0
        ct += 1

        # キューが無くなるまでループ
        while dq:
            cur_y, cur_x = dq.popleft()

            for k in range(8):
                next_y, next_x = cur_y+dy[k], cur_x+dx[k]
                if next_x < 0 or W <= next_x or next_y < 0 or H <= next_y:
                    continue  # マスの外
                if field[next_y][next_x] == ".":
                    continue  # 壁
                if dist[next_y][next_x] != -1:
                    continue  # 訪問済み
                dist[next_y][next_x] = dist[cur_y][cur_x] + 1
                dq.append((next_y, next_x))

print(ct)
