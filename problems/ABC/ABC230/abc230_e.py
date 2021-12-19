def bisc(ok, ng, a):
    while 1 < abs(ok-ng):
        mid = (ok +ng)//2
        if N//mid < a:
            ng = mid
        else:
            ok = mid
    return ok

N = int(input())
st = 1
ans = 0
while st < N:
    a = N //st
    next_st = bisc(st, N+1, a)
    ans += (next_st-st+1)*a
    st = next_st + 1

ans += (N-st+1)
print(ans)
