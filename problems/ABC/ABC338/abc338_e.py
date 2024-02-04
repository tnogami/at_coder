from heapq import heapify, heappop, heappush

N = int(input())
AB = [list(map(int,input().split())) for _ in range(N)]

from_to = []

for a, b in AB:
    a -= 1
    b -= 1
    if a < b:
        from_to.append((a, b))
    else:    
        from_to.append((b, a))

from_to.sort(key=lambda x: x[0])

is_ok = True

end_hq = [from_to[0][1]]

for a, b in from_to[1:]:
    if a < end_hq[0]:
        if b > end_hq[0]:
            is_ok = False
            break
        else:
            heappush(end_hq, b)
    else:
        while end_hq and end_hq[0] < a:
            heappop(end_hq)
        if end_hq:
            if b > end_hq[0]:
                is_ok = False
                break
            else:
                heappush(end_hq, b)
        else:
            heappush(end_hq, b)

if not is_ok:
    print('Yes')
else:
    print('No')

