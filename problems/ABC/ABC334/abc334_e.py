from collections import deque
from tokenize import group

H, W = map(int, input().split())
field = [list(input()) for _ in range(H)]

Nx, Ny = W, H
dist = [[-1 for i in range(Nx)] for j in range(Ny)]  # 距離
dq = deque()
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

# 初期位置の設定
group_idx = 1
for i in range(Ny):
    for j in range(Nx):
        if field[i][j] == '.':
            continue
        if dist[i][j] != -1:
            continue
        dist[i][j] = group_idx
        dq.append((i, j))

        # キューが無くなるまでループ
        while dq:
            cur_y, cur_x = dq.popleft()

            for k in range(4):
                next_y, next_x = cur_y+dy[k], cur_x+dx[k]
                if next_x < 0 or Nx <= next_x or next_y < 0 or Ny <= next_y:
                    continue  # マスの外
                if field[next_y][next_x] == ".":
                    continue  # 壁
                if dist[next_y][next_x] != -1:
                    continue  # 訪問済み
                dist[next_y][next_x] = dist[cur_y][cur_x]
                dq.append((next_y, next_x))

        group_idx += 1

num_group = group_idx - 1

ct = 0
group_sum = 0
for i in range(H):
    for j in range(W):
        if field[i][j] == '#':
            continue

        ct += 1

        group_set = set()
        for k in range(4):
            next_y, next_x = i+dy[k], j+dx[k]
            if next_x < 0 or W <= next_x or next_y < 0 or H <= next_y:
                continue
            if field[next_y][next_x] == '.':
                continue
            group_idx = dist[next_y][next_x]
            group_set.add(group_idx)

        group_sum += num_group - len(group_set) + 1


mod = 998244353
inv = pow(ct, mod-2, mod)

print(group_sum * inv % mod)
