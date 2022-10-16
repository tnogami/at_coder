import bisect
H, W, rs, cs = map(int, input().split())
N = int(input())
r2c = dict()
c2r = dict()
for _ in range(N):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    if r in r2c:
        r2c[r].append(c)
    else:
        r2c[r] = [c]
    if c in c2r:
        c2r[c].append(r)
    else:
        c2r[c] = [r]

for r in r2c.keys():
    r2c[r].sort()

for c in c2r.keys():
    c2r[c].sort()

Q = int(input())

r, c = rs-1, cs-1

for _ in range(Q):
    d, l = input().split()
    l = int(l)
    if d == 'L':
        if r not in r2c:
            can_move = min(c, l)
        else:
            L = r2c[r]
            idx = bisect.bisect(L, c)
            if idx == 0:
                can_move = min(c, l)
            else:
                can_move = min(c - L[idx-1] - 1, l)
        c -= can_move
    elif d == 'R':
        if r not in r2c:
            can_move = min(W - c - 1, l)
        else:
            L = r2c[r]
            idx = bisect.bisect(L, c)
            if idx == len(L):
                can_move = min(W - c - 1, l)
            else:
                can_move = min(L[idx] - c - 1, l)
        c += can_move
    elif d == 'U':
        if c not in c2r:
            can_move = min(r, l)
        else:
            L = c2r[c]
            idx = bisect.bisect(L, r)
            if idx == 0:
                can_move = min(r, l)
            else:
                can_move = min(r - L[idx-1] - 1, l)
        r -= can_move
    elif d == 'D':
        if c not in c2r:
            can_move = min(H - r - 1, l)
        else:
            L = c2r[c]
            idx = bisect.bisect(L, r)
            if idx == len(L):
                can_move = min(H - r - 1, l)
            else:
                can_move = min(L[idx] - r - 1, l)
        r += can_move

    print(r+1, c+1)