H, W = map(int, input().split())
field = [input() for _ in range(H)]
dx = (1,0,-1,0)
dy = (0,-1,0,1)

ans = True
for i in range(H):
    for j in range(W):
        if field[i][j] == ".": continue
        for k in range(4):
            check_x = j + dx[k]
            check_y = i + dy[k]
            if check_x < 0 or W <= check_x or check_y < 0 or H <= check_y: continue
            if field[check_y][check_x] == "#":break
        else:
            ans = False

if ans :
    print("Yes")
else:
    print("No")