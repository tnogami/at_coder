N, Q = map(int, input().split())

# B or W
field = [input() for _ in range(N)]

acc = [[0] * (N + 1) for _ in range(N + 1)]


for i in range(N):
    for j in range(N):
        acc[j + 1][i + 1] = acc[j][i + 1] + acc[j + 1][i] - acc[j][i]
        if field[j][i] == 'B':
            acc[j + 1][i + 1] += 1


sum_B = acc[N][N]

for _ in range(Q):
    x1, y1, x2, y2 = map(int, input().split())
    x2 += 1
    y2 += 1

    ct = 0
    # x1が何個目のfieldか求める
    idx_x1 = x1 // N
    # y1が何個目のfieldか求める
    idx_y1 = y1 // N
    # x2が何個目のfieldか求める
    idx_x2 = x2 // N
    # y2が何個目のfieldか求める
    idx_y2 = y2 // N

    diff_x = max(0, idx_x2 - idx_x1 - 1)
    diff_y = max(0, idx_y2 - idx_y1 - 1)

    ct += sum_B * (diff_x * diff_y)

    # x1, y1が何個目のfieldの何行目か求める
    idx2_x1 = x1 % N
    idx2_y1 = y1 % N
    # x2, y2が何個目のfieldの何行目か求める
    idx2_x2 = x2 % N
    idx2_y2 = y2 % N

    if idx_x1 == idx_x2 and idx_y1 == idx_y2:
        ct += acc[idx2_x2][idx2_y2] - acc[idx2_x1][idx2_y2] - \
            acc[idx2_x2][idx2_y1] + acc[idx2_x1][idx2_y1]
        print(ct)
        continue
    elif idx_x1 == idx_x2:
        ct += acc[idx2_x2][N] - acc[idx2_x1][N] - \
            acc[idx2_x2][idx2_y1] + acc[idx2_x1][idx2_y1]
        ct += (acc[idx2_x2][N] - acc[idx2_x1][N]) * diff_y
        ct += acc[idx2_x2][idx2_y2] - acc[idx2_x1][idx2_y2]
        print(ct)
        continue
    elif idx_y1 == idx_y2:
        ct += acc[N][idx2_y2] - acc[N][idx2_y1] - \
            acc[idx2_x1][idx2_y2] + acc[idx2_x1][idx2_y1]
        ct += (acc[N][idx2_y2] - acc[N][idx2_y1]) * diff_x
        ct += acc[idx2_x2][idx2_y2] - acc[idx2_x2][idx2_y1]
        print(ct)
        continue

    # 4角を足す
    ct += acc[N][N] - acc[idx2_x1][N] - acc[N][idx2_y1] + acc[idx2_x1][idx2_y1]
    ct += acc[idx2_x2][idx2_y2]
    ct += acc[idx2_x2][N] - acc[idx2_x2][idx2_y1]
    ct += acc[N][idx2_y2] - acc[idx2_x1][idx2_y2]

    # 4辺を足す
    ct += (acc[N][N] - acc[N][idx2_y1]) * diff_x
    ct += (acc[N][N] - acc[idx2_x1][N]) * diff_y
    ct += (acc[N][idx2_y2]) * diff_x
    ct += (acc[idx2_x2][N]) * diff_y

    print(ct)
