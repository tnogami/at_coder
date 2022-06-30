X, Y, A, B = map(int, input().split())

ans = 0

while X*A < X+B:
    if Y <= X * A : break
    X *= A
    ans += 1

ans += ((Y-1)-X)//B

print(ans)
    


