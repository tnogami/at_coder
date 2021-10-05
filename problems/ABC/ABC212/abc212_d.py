import heapq

Q = int(input())

add = 0
balls = []
heapq.heapify(balls) 
for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 3:
        print(heapq.heappop(balls)+add)
    elif q[0] == 1:
        j = q[1]-add
        heapq.heappush(balls, j)
    else:
        add += q[1]
