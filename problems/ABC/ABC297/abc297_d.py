A, B = map(int, input().split())

ans = 0

while True:
    if A > B:
        can_minus = -(-(A - B)//B)
        A -= can_minus*B
        ans += can_minus
    elif A < B:    
        can_minus = -(-(B - A)//A)
        B -= can_minus*A
        ans += can_minus
    elif A == B:
        break

print(ans)