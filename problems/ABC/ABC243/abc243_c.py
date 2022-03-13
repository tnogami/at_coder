from collections import defaultdict

xtoy = defaultdict(list)

N = int(input())
XY_tmp = [tuple(map(int, input().split())) for i in range(N)]
S = input()

for i, p in enumerate(XY_tmp):
    xtoy[p[1]].append((p[0],S[i]))

ans = False
for d in xtoy.values():
    d.sort(key=lambda x: x[0])
    r_flag = False
    for _d in d:
        if r_flag and _d[1] == "L":
            ans = True
            break
        if _d[1] == "R":r_flag=True

if ans:
    print("Yes")
else:
    print("No")