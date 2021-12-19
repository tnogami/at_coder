N, D = map(int, input().split())
LR = [tuple(map(int,input().split())) for i in range(N)]

LR.sort()

ct = 1
right = LR[0][1]
for l, r in LR:
    right = min(right, r)
    if D <= l - right:
        ct += 1
        right = r

print(ct)