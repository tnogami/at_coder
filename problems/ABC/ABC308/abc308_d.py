from collections import deque

H, W = map(int, input().split())

S = [input() for _ in range(H)]

dist = [[-1 for i in range(W)] for j in range(H)]  # 距離
dq = deque()
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

# 始点の設定
dq.append((0, 0))
dist[0][0] = 0

snuke = 'snuke'

# キューが無くなるまでループ
while dq:
    cur_y, cur_x = dq.popleft()

    for k in range(4):
        next_y, next_x = cur_y+dy[k], cur_x+dx[k]
        next_string = snuke[(dist[cur_y][cur_x]+1) % 5]
        if next_x < 0 or W <= next_x or next_y < 0 or H <= next_y:
            continue  # マスの外
        if dist[next_y][next_x] != -1:
            continue  # 訪問済み
        if S[next_y][next_x] != next_string:
            continue

        dist[next_y][next_x] = dist[cur_y][cur_x] + 1
        dq.append((next_y, next_x))

if dist[H-1][W-1] != -1:
    print("Yes")
else:
    print("No")