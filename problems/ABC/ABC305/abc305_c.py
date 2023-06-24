H, W = map(int, input().split())
field = [input() for _ in range(H)]

dy = (1,0,-1,0)
dx = (0,1,0,-1)
for i in range(H):
    for j in range(W):
        if field[i][j] == '#': continue
        ct = 0
        for k in range(4):
            y = i + dy[k]
            x = j + dx[k]
            if x < 0 or W <= x or y < 0 or H <= y:continue
            if field[y][x] == '#': ct += 1
        
        if 2 <= ct:
            print(i+1, j+1)