from collections import deque
import math

N, M = map(int, input().split())
moves = set()

K = int(math.sqrt(M))+3
for a in range(K):
    for b in range(K):
        if a**2+b**2 == M:
            moves.add((a,b))
            moves.add((-a,b))
            moves.add((a,-b))
            moves.add((-a,-b))


dist = [[-1 for i in range(N)] for j in range(N)] #距離
dq = deque()

# 始点の設定
dq.append((0,0))
dist[0][0] = 0

#キューが無くなるまでループ
while dq:
    cur_y, cur_x = dq.popleft()

    for move in moves:
        next_y, next_x = cur_y+move[0], cur_x+move[1]
        if next_x < 0 or N <= next_x or next_y < 0 or N <= next_y : continue #マスの外
        if dist[next_y][next_x] != -1 : continue #訪問済み
        dist[next_y][next_x] = dist[cur_y][cur_x] + 1
        dq.append((next_y,next_x))

for d in dist:
    print(*d)