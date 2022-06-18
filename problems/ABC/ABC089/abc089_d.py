from itertools import accumulate
H, W, D = map(int, input().split())
field = [tuple(map(int, input().split())) for _ in range(H)]

d = dict()

for i in range(H):
    for j in range(W):
        n = field[i][j]
        d[n] = (i,j)

table = [[0] for _ in range(D)]
for p in range(1, D+1):
    m = p + D
    pre = p
    while m <= H*W:
        table[p%D].append(abs(d[pre][0]-d[m][0])+abs(d[pre][1]-d[m][1]))
        pre = m
        m += D

for i in range(len(table)):
    table[i] = list(accumulate(table[i]))

Q = int(input())

for _ in range(Q):
    l, r = map(int, input().split())
    if l%D == 0:
        print(table[l%D][r//D-1]-table[l%D][l//D-1])
    else:
        print(table[l%D][r//D]-table[l%D][l//D])