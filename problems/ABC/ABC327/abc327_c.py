field = [list(map(int, input().split())) for _ in range(9)]

is_ok = True

for i in range(9):
    tmp = field[i]
    if len(set(tmp)) != 9:
        is_ok = False
        break

for j in range(9):
    tmp = [field[i][j] for i in range(9)]
    if len(set(tmp)) != 9:
        is_ok = False
        break

for i, j in [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6), ]:
    tmp = []
    for k in range(3):
        for l in range(3):
            tmp.append(field[i+k][j+l])

    if len(set(tmp)) != 9:
        is_ok = False
        break

if is_ok:
    print("Yes")
else:
    print("No")
