from heapq import heappush, heappop, heapify

N, M = map(int, input().split())
tops = list(range(N))
heapify(tops)
top = 0
amounts = [0] * N
absents = []
s_absents = set()

for _ in range(M):
    t, w, s = map(int, input().split())
    while absents:
        t_back, idx = absents[0]
        if t_back <= t:
            heappop(absents)
            heappush(tops, idx)
            s_absents.remove(idx)
            if idx < top:
                top = idx
        else:
            break

    if top == N:
        continue

    amounts[top] += w
    heappush(absents, (t + s, top))
    s_absents.add(top)

    while True:
        if not tops:
            top = N
            break
        else:
            idx = tops[0]
            if idx in s_absents:
                heappop(tops)
            else:
                top = idx
                break

for a in amounts:
    print(a)
