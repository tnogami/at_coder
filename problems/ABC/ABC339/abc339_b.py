H, W, N = map(int, input().split())

field = [['.']*W for _ in range(H)]
urdl = [(-1, 0), (0, 1), (1, 0), (0, -1)]

pos = [0, 0]
direction_idx = 0

for _ in range(N):
    if field[pos[0]][pos[1]] == '.':
        field[pos[0]][pos[1]] = '#'
        direction_idx = (direction_idx + 1) % 4
        pos[0] += urdl[direction_idx][0]
        pos[1] += urdl[direction_idx][1]
        pos[0] %= H
        pos[1] %= W
    else:
        field[pos[0]][pos[1]] = '.'
        direction_idx = (direction_idx - 1) % 4
        pos[0] += urdl[direction_idx][0]
        pos[1] += urdl[direction_idx][1]
        pos[0] %= H
        pos[1] %= W

for f in field:
    print(''.join(f))

