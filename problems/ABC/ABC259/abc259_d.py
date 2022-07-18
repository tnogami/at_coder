from itertools import combinations
N = int(input())
sx, sy, tx, ty = map(int, input().split())

XYR = [tuple(map(int, input().split())) for _ in range(N)]

nodes = [[] for _ in range(N)]

for i, j in combinations(range(N), 2):
    x1 = XYR[i][0]
    y1 = XYR[i][1]
    r1 = XYR[i][2]
    x2 = XYR[j][0]
    y2 = XYR[j][1]
    r2 = XYR[j][2]
    d2 = (x1-x2)**2 + (y1-y2)**2
    if abs(r1-r2)**2 <= d2 and d2 <= (r1+r2)**2:
        nodes[i].append(j)
        nodes[j].append(i)

print(nodes)

goal = []
start = []
for i in range(N):
    x, y, r = XYR[i]
    if (sx-x)**2 + (sy-y)**2 == r**2:
        start.append(i)
    
    if (tx-x)**2 + (ty-y)**2 == r**2:
        goal.append(i)

for s in start:
    



