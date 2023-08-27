from collections import deque
N, M = map(int, input().split())
field = [input() for _ in range(N)]
stopped = [[False] * M for _ in range(N)]
breaked = [[False] * M for _ in range(N)]

dq = deque()
dq.append((1, 1))
stopped[1][1] = True
breaked[1][1] = True

while dq:
    x, y = dq.popleft()

    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        if field[nx][ny] == '#':
            continue

        breaked[nx][ny] = True

        mult = 2

        while True:
            nx, ny = x + mult*dx, y + mult*dy
            if field[nx][ny] == '#':
                nx, ny = nx - dx, ny - dy
                break

            breaked[nx][ny] = True
            mult += 1

        if not stopped[nx][ny]:
            stopped[nx][ny] = True
            dq.append((nx, ny))
ans = 0
for i in range(N):
    for j in range(M):
        if breaked[i][j]:
            ans += 1
print(ans)
