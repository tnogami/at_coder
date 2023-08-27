from itertools import permutations
N, M = map(int, input().split())
P = []

for _ in range(N):
    tmp = list(map(int, input().split()))
    p = tmp[0]
    c = tmp[1]
    f = set(tmp[2:])
    P.append((p, c, f))

flag = False
for ps in permutations(P, 2):
    p1 = ps[0]
    p2 = ps[1]
    if not (p1[0] <= p2[0]):
        continue
    if not (p1[2] >= p2[2]):
        continue
    if not ((p1[0] < p2[0]) or (p1[2] > p2[2])):
        continue
    flag = True

if flag:
    print("Yes")
else:
    print("No")
