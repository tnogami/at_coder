X, A, D, N = map(int, input().split())
X -= A
if D < 0:
    D *= -1
    X *= -1

if 0 < D:
    n = X//D
    if n < 0:
        print(-X)
    elif N-1 < n:
        print(X-(N-1)*D)
    else:
        print(min(X-n*D, (n+1)*D-X))
else:
    print(abs(X))



