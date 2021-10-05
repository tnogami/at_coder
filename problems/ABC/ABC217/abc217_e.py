import heapq
import collections

Q = int(input())
a = []
heapq.heapify(a)
b = collections.deque()

for i in range(Q):
    n = list(map(int, input().split()))
    if n[0] == 1:
        b.append(n[1])
    elif n[0] == 2:
        if a:
            print(heapq.heappop(a))
        else:
            print(b.popleft())
    else:
        while b:
            heapq.heappush(a, b.popleft())

