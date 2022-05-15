sx, sy, gx, gy = map(int, input().split())

gy = -gy

t = (gx-sx)/(gy-sy)

print(sx-sy*t)