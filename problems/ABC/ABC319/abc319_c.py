from itertools import permutations
c = [list(map(int, input().split())) for _ in range(3)]


def C(idx):
    return c[idx//3][idx % 3]


def ij2idx(i, j):
    return 3*j + i


ngs = []

for j in range(3):
    if c[j][0] == c[j][1]:
        ngs.append((ij2idx(0, j), ij2idx(1, j), ij2idx(2, j)))
    elif c[j][0] == c[j][2]:
        ngs.append((ij2idx(0, j), ij2idx(2, j), ij2idx(1, j)))
    if c[j][1] == c[j][2]:
        ngs.append((ij2idx(1, j), ij2idx(2, j), ij2idx(0, j)))

for i in range(3):
    if c[0][i] == c[1][i]:
        ngs.append((ij2idx(i, 0), ij2idx(i, 1), ij2idx(i, 2)))
    elif c[0][i] == c[2][i]:
        ngs.append((ij2idx(i, 0), ij2idx(i, 2), ij2idx(i, 1)))
    if c[1][i] == c[2][i]:
        ngs.append((ij2idx(i, 1), ij2idx(i, 2), ij2idx(i, 0)))

if c[0][0] == c[1][1]:
    ngs.append((ij2idx(0, 0), ij2idx(1, 1), ij2idx(2, 2)))
elif c[0][0] == c[2][2]:
    ngs.append((ij2idx(0, 0), ij2idx(2, 2), ij2idx(1, 1)))
if c[1][1] == c[2][2]:
    ngs.append((ij2idx(1, 1), ij2idx(2, 2), ij2idx(0, 0)))

if c[0][2] == c[1][1]:
    ngs.append((ij2idx(2, 0), ij2idx(1, 1), ij2idx(0, 2)))
elif c[0][2] == c[2][0]:
    ngs.append((ij2idx(2, 0), ij2idx(0, 2), ij2idx(1, 1)))
if c[1][1] == c[2][0]:
    ngs.append((ij2idx(1, 1), ij2idx(0, 2), ij2idx(2, 0)))

ngs = set(ngs)
ct = 0
for order in permutations(range(9), 9):
    opened = set()
    flag = False
    for idx in order:
        opened.add(idx)
        for ng in ngs:
            if ng[0] in opened and ng[1] in opened and ng[2] not in opened:
                ct += 1
                flag = True
                break
        if flag:
            break

print(1-ct/(9*8*7*6*5*4*3*2))
