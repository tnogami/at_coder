Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())
Cx, Cy = map(int, input().split())
Dx, Dy = map(int, input().split())

AB = (Bx-Ax, By-Ay)
BA = (Ax-Bx, Ay-By)

BC = (Cx-Bx, Cy-By)
CB = (Bx-Cx, By-Cy)

CD = (Dx-Cx, Dy-Cy)
DC = (Cx-Dx, Cy-Dy)

DA = (Ax-Dx, Ay-Dy)
AD = (Dx-Ax, Dy-Ay)

def f(a,b):
    return a[0]*b[1]-a[1]*b[0]

print(f(BA,BC))
print(f(BA,BC))
print(f(BA,BC))
print(f(BA,BC))

if 0 <= f(BC,BA) and 0 <= f(CD, CB) and 0 <= f(DA, DC) and 0 <= f(AB, AD):
    print("Yes")
else:
    print("No")

