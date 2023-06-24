from heapq import heappop, heappush

N, M, K = map(int, input().split())

nodes = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    nodes[a-1].append(b-1)
    nodes[b-1].append(a-1)


hq = []
for _ in range(K):
    pos, hp = map(int, input().split())
    heappush(hq, (-hp, pos-1))

visited = [False]*N
while hq:
    hp, pos = heappop(hq)
    if visited[pos]:
        continue

    visited[pos] = True

    if hp == 0:
        continue

    for to in nodes[pos]:
        if visited[to]: continue
        heappush(hq, (hp+1, to))

ct = 0
ans = []
for i, v in enumerate(visited, 1):
    if v:
        ct += 1
        ans.append(i)

print(ct)
print(*ans)