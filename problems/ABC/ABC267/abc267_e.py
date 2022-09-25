from heapq import heappop, heappush

N, M = map(int, input().split())
A = list(map(int,input().split()))
nodes = [[] for _ in range(N)]
edges = []

for _ in range(M):
    a, b = map(int, input().split())
    edges.append((a-1,b-1))
    nodes[a-1].append(b-1)
    nodes[b-1].append(a-1)

hq = []
costs = [0]*N
deleted = [False]*N
deleted_ct = 0

for edge in edges:
    i, j = edge
    costs[i] += A[j]
    costs[j] += A[i]

for i, c in enumerate(costs):
    heappush(hq, (c,i))

ans = 0

while deleted_ct < N:
    c, i = heappop(hq)
    if deleted[i]:continue

    deleted[i] = True
    ans = max(ans, costs[i])
    deleted_ct += 1

    for to in nodes[i]:
        if deleted[to]:continue
        costs[to] -= A[i]
        heappush(hq, (costs[to],to))
    
print(ans)