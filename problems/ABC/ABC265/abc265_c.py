H, W = map(int, input().split())
field = [input() for _ in range(H)]
visited = [[False]*W for _ in range(H)]
cur_x, cur_y = 0, 0

while True:
    if field[cur_y][cur_x] == "U":
        next_x, next_y = cur_x, cur_y - 1

    elif field[cur_y][cur_x] == "D":
        next_x, next_y = cur_x, cur_y + 1

    elif field[cur_y][cur_x] == "L":
        next_x, next_y = cur_x - 1, cur_y

    else:
        next_x, next_y = cur_x + 1, cur_y

    if next_x < 0 or W <= next_x or next_y < 0 or H <= next_y :
        print(cur_y+1, cur_x+1)
        break
    elif visited[next_y][next_x]:
        print(-1)
        break
    else:
        visited[next_y][next_x] = True
        cur_x, cur_y = next_x, next_y

