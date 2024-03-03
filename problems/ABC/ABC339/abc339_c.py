N = int(input())
A = list(map(int,input().split()))

A = A[::-1]
s = sum(A)

ng = -1
ok = 10**18

def check(num):
    is_ok = True
    for a in A:
        num -= a
        if num < 0:
            is_ok = False
            break

    return is_ok

while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)