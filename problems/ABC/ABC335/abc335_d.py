N = int(input())
field = [[-1]*N for _ in range(N)]

# 外から渦巻き状に番号を振る
num = 1
field [0][0] = num
direction = ['R', 'D', 'L', 'U']
cur_dir = 'R'
cur_x = 0
cur_y = 0

while True:
    if cur_dir == 'R':
        if cur_x+1 < N and field[cur_y][cur_x+1] == -1:
            num += 1
            cur_x += 1
            field[cur_y][cur_x] = num
        else: # 方向転換
            cur_dir = 'D'
    elif cur_dir == 'D':
        if cur_y+1 < N and field[cur_y+1][cur_x] == -1:
            num += 1
            cur_y += 1
            field[cur_y][cur_x] = num
        else:
            cur_dir = 'L'
    elif cur_dir == 'L':
        if cur_x-1 >= 0 and field[cur_y][cur_x-1] == -1:
            num += 1
            cur_x -= 1
            field[cur_y][cur_x] = num
        else:
            cur_dir = 'U'
    elif cur_dir == 'U':
        if cur_y-1 >= 0 and field[cur_y-1][cur_x] == -1:
            num += 1
            cur_y -= 1
            field[cur_y][cur_x] = num
        else:
            cur_dir = 'R'
    if num == N*N:
        break

field[(N+1)//2-1][(N+1)//2-1] = 'T'
for f in field:
    print(*f)

