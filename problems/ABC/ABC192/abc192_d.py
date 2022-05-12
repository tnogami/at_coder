input_count = 0

def is_ok(mid):
    num = 0
    for i, x in enumerate(X[::-1]):
        num += int(x)*mid**i
    return num <= M

X = input()
M = int(input())

d = max(map(int, list(X)))

if len(X) == 1:
    if int(X, d+1) <= M:
        print(1)
    else:
        print(0)
elif M < int(X, d+1):
    print(0)
else:
    ng = 10**24
    ok = d+1
    while 1 < abs(ok-ng):
        mid = (ok+ng)//2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    print(ok-d)
            