import collections

H, W = map(int, input().split())
ch, cw = map(int, input().split())
dh, dw = map(int, input().split())

dy = (-2, -1, 0, 1, 2)
dx = (-2, -1, 0, 1, 2)

field = [input() for i in range(H)]
dist = [[10**9 for i in range(W)] for j in range(H)]
dist[ch-1][cw-1] = 0

dq = collections.deque()
dq.append((ch-1, cw-1))

while dq:
    cur_y, cur_x = dq.pop()

    for i in range(5):
        for j in range(5):
            next_y, next_x = cur_y + dy[i], cur_x + dx[j]
            if next_x < 0 or W <= next_x or next_y < 0 or H <= next_y : continue #マスの外
            if field[next_y][next_x] == "#" : continue #壁

            if abs(dy[i]) + abs(dx[j]) <= 1:
                if dist[cur_y][cur_x] < dist[next_y][next_x]: 
                    dist[next_y][next_x] = dist[cur_y][cur_x]
                    dq.append((next_y,next_x))
            else:
                if dist[cur_y][cur_x] + 1 < dist[next_y][next_x]:
                    dist[next_y][next_x] = dist[cur_y][cur_x] + 1
                    dq.appendleft((next_y,next_x))

ans = dist[dh-1][dw-1]
if ans == 10**9:
    print(-1)
else:
    print(ans)