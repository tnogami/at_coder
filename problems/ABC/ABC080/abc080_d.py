from heapq import heapify, heappop, heappush

N, C = map(int, input().split())
stc = [tuple(map(int, input().split())) for _ in range(N)]

recorder = []
heapify(recorder)

stc.sort()

ans = 0

for s,t,c in stc:
  
    checked = []
    while recorder:
        end_time, ch = heappop(recorder)
        if c == ch or end_time < s - 0.5:
            continue
        else:
            checked.append((end_time, ch))

    for ck in checked:
        heappush(recorder, ck)

    heappush(recorder, (t,c))

    ans = max(ans, len(recorder))

print(ans)
