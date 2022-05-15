r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r = r2 - r1
c = c2 - c1
if r == 0 and c ==0:
    print(0)
elif c+r == 0 or c-r == 0 or abs(r)+abs(c) <= 3:
    print(1)
elif (r+c)%2 == 0 or (r-3<=c and c<=r+3) or (-r-3<=c and c<=-r+3) or abs(r)+abs(c) <= 6:
    print(2)
else:
    print(3)