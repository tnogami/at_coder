import heapq

N, M = map(int, input().split())
A = list(map(lambda x : -1*int(x),input().split()))

hq = A
heapq.heapify(hq)

for i in range(M):
    n = heapq.heappop(hq)
    n *= -1
    n = n//2
    n *= -1
    heapq.heappush(hq, n)

print(-sum(hq))
