import heapq
N, L = map(int, input().split())
A = list(map(int,input().split()))
if L != sum(A):
    A.append(L-sum(A))
heapq.heapify(A)
cost = 0
while 1 < len(A):
    a = heapq.heappop(A)
    b = heapq.heappop(A)
    cost += a+b
    heapq.heappush(A,a+b)

print(cost)