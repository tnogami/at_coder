
Ha, Wa = map(int, input().split())
A = [input() for _ in range(Ha)]

Hb, Wb = map(int, input().split())
B = [input() for _ in range(Hb)]

Hx, Wx = map(int, input().split())
X = [input() for _ in range(Hx)]

ans = False

tmp = []

for h in range(Hx):
    for w in range(Wx):
        if X[h][w] == "#":
            tmp.append((h+10, w+10))

f_set = frozenset(tmp)

for ha in range(0, 20):
    for wa in range(0, 20):
        for hb in range(0, 20):
            for wb in range(0, 20):
                # ここまでオフセット

                # チェック
                flag = True
                tmp = []
                for h in range(Ha):
                    for w in range(Wa):
                        if A[h][w] == '#':
                            tmp.append((h+ha, w+wa))

                for h in range(Hb):
                    for w in range(Wb):
                        if B[h][w] == '#':
                            tmp.append((h+hb, w+wb))

                _fset = frozenset(list(set(tmp)))

                if f_set == _fset:
                    ans = True

                if ans:
                    break

if ans:
    print("Yes")
else:
    print("No")
