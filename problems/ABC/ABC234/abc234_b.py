
import math
N = int(input())
xy = [tuple(map(int,input().split())) for i in range(N)]

ans = 0
for i in range(0, N-1):
    for j in range(i, N):
        d2 = (xy[i][0]-xy[j][0])**2+(xy[i][1]-xy[j][1])**2

        ans = max(ans, d2)
print(math.sqrt(ans))