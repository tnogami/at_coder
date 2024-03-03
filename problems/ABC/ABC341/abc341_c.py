H, W, N = map(int, input().split())
T = input()
field = [input() for _ in range(H)]
ans = 0
for i in range(H):
    for j in range(W):
        if field[i][j] == '#':
            continue

        x = j
        y = i

        for t in T:
            if t == 'L':
                x -= 1
            elif t == 'R':
                x += 1
            elif t == 'U':
                y -= 1
            elif t == 'D':
                y += 1
        
            if field[y][x] == '#':
                break
        else:
            ans += 1

print(ans)