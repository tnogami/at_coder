from collections import deque

N, M = map(int, input().split())
nodes = [[set(), set()] for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    nodes[u-1][0].add(v-1)
    nodes[v-1][1].add(u-1)

que = deque([i for i in range(N) if len(nodes[i][0]) == 0])
ans = [True]*N
while que:
    i = que.popleft()
    ans[i] = False
    for frm in nodes[i][1]:
        if i in nodes[frm][0]:
            nodes[frm][0].remove(i)
            if len(nodes[frm][0]) == 0:
                que.append(frm)

print(ans.count(True))