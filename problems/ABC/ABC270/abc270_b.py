X, Y, Z = map(int, input().split())
if X < 0:
    X *= -1
    Y *= -1
    Z *= -1

if Y < 0 or X < Y:
    print(X)
else:
    if Z < 0:
        print(-2*Z+X)
    else:
        if Z < Y:
            print(X)
        else:
            print(-1)

