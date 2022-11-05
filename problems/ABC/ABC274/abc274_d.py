N, X, Y = map(int, input().split())
A = list(map(int,input().split()))
Ax = []
Ay = []

for i, a in enumerate(A):
    if i%2 == 0:
        Ax.append(a)
    else:
        Ay.append(a)

dpx = [[False]*(10*2*len(Ax)+5) for _ in range(len(Ax)+1)]
dpy = [[False]*(10*2*len(Ay)+5) for _ in range(len(Ay)+1)]

midx = (10*2*len(Ax)+5)//2
midy = (10*2*len(Ay)+5)//2

dpx[1][midx+A[0]] = True
dpy[0][midy] = True

for n in range(len(Ax)-1):
    a = Ax[n+1]
    for pos in range(10*2*len(Ax)+5):
        if dpx[n+1][pos]:
            dpx[n+2][pos+a] = True
            dpx[n+2][pos-a] = True


for n in range(len(Ay)):
    a = Ay[n]
    for pos in range(10*2*len(Ay)+5):
        if dpy[n][pos]:
            dpy[n+1][pos+a] = True
            dpy[n+1][pos-a] = True

if dpx[-1][midx+X] and dpy[-1][midy+Y]:
    print("Yes")
else:
    print("No")