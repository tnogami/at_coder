from bisect import bisect_left, bisect
N, M, K = map(int, input().split())
AB = [list(map(int,input().split())) for _ in range(N)]
CD = [list(map(int,input().split())) for _ in range(M)]

ok = 1
ng = 0
    
for _ in range(100):
    mid = (ok+ng)/2.0
    sugr_req = []
    for c, d in CD:
        sugr_req.append(c-(mid*d)/(1-mid))
    sugr_req.sort()

    ct = 0
    for a, b in AB:
        ex_suger = a-(mid*b)/(1-mid)
        req_suger = -ex_suger
        ct += M - bisect_left(sugr_req, req_suger)

    if K <= ct:
        ng = mid
    else:
        ok = mid

print(mid*100)


