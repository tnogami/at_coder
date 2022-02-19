import math
x1, y1, x2, y2 = map(int, input().split())

dx = (1,2,1,2,-1,-1,-2,-2)
dy = (2,1,-2,-1,2,-2,1,-1)

set1 = set()
set2 = set()

for i in range(8):
    set1.add((x1+dx[i], y1+dy[i]))
    set2.add((x2+dx[i], y2+dy[i]))

if set1&set2:
    print("Yes")
else:
    print("No")