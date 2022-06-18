

from collections import deque
from itertools import chain

H, W = map(int, input().split())
dq = deque()
dx = (0,1,0,-1)
dy = (1,0,-1,0)

#fieldの入力
field = [input() for j in range(H)]
ans = 0

for j in range(W):
    for i in range(H):

        if field[i][j] == "#": continue

        dist = [[-1 for i in range(W)] for j in range(H)] #距離

        # 始点の設定
        dq.append((i,j))
        dist[i][j] = 0

        #キューが無くなるまでループ
        while dq:
            cur_y, cur_x = dq.popleft()

            for k in range(4):
                next_y, next_x = cur_y+dy[k], cur_x+dx[k]
                if next_x < 0 or W <= next_x or next_y < 0 or H <= next_y : continue #マスの外
                if field[next_y][next_x] == "#" : continue #壁
                if dist[next_y][next_x] != -1 : continue #訪問済み
                dist[next_y][next_x] = dist[cur_y][cur_x] + 1
                dq.append((next_y,next_x))

        ans = max(ans, max(chain(*dist)))

print(ans)