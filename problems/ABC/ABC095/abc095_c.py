A, B, C, X, Y = map(int, input().split())
ans = 0
if 2*C <= A+B:
    if X < Y:
        ans += X*2*C
        Y -= X
        if 2*C < B:
            ans += Y*2*C
        else:
            ans += Y*B
    else:
        ans += Y*2*C
        X -= Y
        if 2*C < A:
            ans += X*2*C
        else:
            ans += X*A
    print(ans)
else:
    print(X*A+Y*B)
    


    