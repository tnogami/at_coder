A, B, C, D, E, F, X = map(int, input().split())
X1 = X
X2 = X
t = 0
a = 0
for i in range(1000):
    if A < X1 :
        X1 -= A
        t += A*B
    else:
        t += X1*B
        X1 -= X1
    X1 -= C
    if X1 <= 0: break

for i in range(1000):
    if D < X2 :
        X2 -= D
        a += D*E
    else:
        a += X2*E
        X2 -= X2
    X2 -= F
    if X2 <= 0: break

if t == a:
    print("Draw")
elif t>a:
    print("Takahashi")
else:
    print("Aoki")