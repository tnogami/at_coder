H, W, X, Y = map(int, input().split())

field = [input() for i in range(H)]
count = -3
for i in range(X-1, H, 1):
    if field[i][Y-1] == "#":break
    count += 1

for i in range(X-1, -1, -1):
    if field[i][Y-1] == "#":break
    count += 1

for i in range(Y-1, W, 1):
    if field[X-1][i] == "#":break
    count += 1

for i in range(Y-1, -1, -1):
    if field[X-1][i] == "#":break
    count += 1

print(count)
