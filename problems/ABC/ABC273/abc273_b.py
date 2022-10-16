X, K = map(int, input().split())

if len(str(X)) < K:
    print(0)
else:
    for i in range(K):
        s = str(X)
        if 5 <= int(s[-(i+1)]):
            X //= 10**(i+1)
            X += 1
            X *= 10**(i+1)
        else:
            X //= 10**(i+1)
            X *= 10**(i+1)
    
    print(X)
