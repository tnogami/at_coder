from heapq import heappush, heappop
OUT = 0
IN = 1

N, M = map(int, input().split())
nodes = [[set([]) for j in range(2)] for i in range(N)]
ans = []

for i in range(M):
    A, B = map(int, input().split())
    nodes[A-1][OUT].add(B-1)
    nodes[B-1][IN].add(A-1)

hq = []

for i in range(N):
    if len(nodes[i][IN]) == 0:
        heappush(hq, i)

while hq:
    a = heappop(hq)
    ans.append(str(a+1))
    for to in nodes[a][OUT]:
        nodes[to][IN].remove(a)
        if len(nodes[to][IN]) == 0:
            heappush(hq, to)

if len(ans) == N:

    print(" ".join(ans))
else:
    print(-1)

