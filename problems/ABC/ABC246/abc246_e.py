from collections import deque
N = int(input())
Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())
field = [input() for _ in range(N)]

dist = [[-1 for i in range(N)] for j in range(N)] #距離
que = deque()
dx = (1,1,-1,-1)
dy = (1,-1,1,-1)

# 始点の設定
que.append((Ax-1,Ay-1))
dist[Ax-1][Ay-1] = 0

#キューが無くなるまでループ
while que:
    cur_x, cur_y = que.popleft()

    for k in range(4):
        next_y, next_x = cur_y, cur_x
        while True:
            next_y, next_x = next_y+dy[k], next_x+dx[k]
            if next_x < 0 or N <= next_x or next_y < 0 or N <= next_y : break #マスの外
            if field[next_x][next_y] == "#" : break #壁
            if dist[next_x][next_y] != -1 and dist[cur_x][cur_y] >= dist[next_x][next_y]: break #訪問済み
            if dist[next_x][next_y] != -1 and dist[cur_x][cur_y] + 1 == dist[next_x][next_y]: continue #訪問済み
            dist[next_x][next_y] = dist[cur_x][cur_y] + 1
            que.append((next_x,next_y))

print(dist[Bx-1][By-1])