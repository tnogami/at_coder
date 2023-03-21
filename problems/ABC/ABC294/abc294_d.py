from heapq import heappop, heappush
N, Q = map(int, input().split())

not_called = list(range(N, 0, -1))
called = []
done = set([])

ans = []
for _ in range(Q):
    event = list(map(int,input().split()))

    if event[0] == 1:
        a = not_called.pop()
        heappush(called, a)
    elif event[0] == 2:
        done.add(event[1])
    else:
        while True:
            a = heappop(called)
            if a in done: continue
            ans.append(a)
            heappush(called, a)
            break

for a in ans:
    print(a)


