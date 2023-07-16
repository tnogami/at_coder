field = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

a, b = map(int, input().split())


for i in range(3):
    for j in range(3):
        if a == field[i][j]:
            a_pos = [i, j]
        if b == field[i][j]:
            b_pos = [i, j]

dx = (0, 0)
dy = (1, -1)

flag = False
for k in range(2):
    if a_pos == [b_pos[0]+dx[k], b_pos[1]+dy[k]]:
        flag = True

if flag:
    print("Yes")
else:
    print("No")
