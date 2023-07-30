N, M = map(int, input().split())
sellers = list(map(int, input().split()))
buyers = list(map(int, input().split()))


def f(mid):
    ct_seller = 0
    ct_buyer = 0
    for s in sellers:
        if s <= mid:
            ct_seller += 1

    for b in buyers:
        if mid <= b:
            ct_buyer += 1

    return ct_seller >= ct_buyer


ok = 10**10
ng = 0

while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if f(mid):
        ok = mid
    else:
        ng = mid

print(ok)
