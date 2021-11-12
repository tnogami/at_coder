import math
N = int(input())
xy = [tuple(map(int,input().split())) for i in range(N)]
magics = set([])

for i in range(N-1):
    for j in range(i+1, N):
        mx = xy[i][0]- xy[j][0]
        my = xy[i][1]- xy[j][1]
        div = math.gcd(abs(mx), abs(my))
        if div != 0:
            magics.add((mx//div, my//div))
            magics.add((-mx//div, -my//div))
        else:
            if mx == 0:
                magics.add((0, 1))
                magics.add((0, -1))
            else:
                magics.add((1, 0))
                magics.add((-1, 0))

print(len(magics))

