#幅優先探索(グリッド)
import queue

H, W = map(int, input().split())
dist = [[-1 for i in range(W)] for j in range(H)] #距離
que = queue.Queue()
dx = (0,1)
dy = (1,0)

#fieldの入力
field = [input() for j in range(H)]

# 始点の設定
que.put((0,0))
dist[0][0] = 0

#キューが無くなるまでループ
while not que.empty():
    cur_y, cur_x = que.get()

    for k in range(2):
        next_y, next_x = cur_y+dy[k], cur_x+dx[k]
        if next_x < 0 or W <= next_x or next_y < 0 or H <= next_y : continue #マスの外
        if field[next_y][next_x] == "#" : continue #壁
        if dist[next_y][next_x] != -1 : continue #訪問済み
        dist[next_y][next_x] = dist[cur_y][cur_x] + 1
        que.put((next_y,next_x))

ans = 0
for d in dist:
    ans = max(ans, max(d))

print(ans+1)

