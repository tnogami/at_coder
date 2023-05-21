from collections import defaultdict
from collections import deque
from dis import dis


N, M = map(int, input().split())
nodes = [set() for _ in range(N+M)]

groups = []
num2group = dict()
start = set()
goal = set()

for n in range(N):
    A = int(input())
    S = set(map(int,input().split()))
    groups.append(S)
    if M in S:
        goal.add(n)
    if 1 in S:
        start.add(n)

    for e in S:
        nodes[n].add(N-1+e)
        nodes[N-1+e].add(n)


if 0 < len(start & goal):
    print(0)
else:
    dist = [-1 for _ in range(N+M)] #距離

    dq = deque()

    # 始点の設定
    for s in start:
        dq.append(s)
        dist[s] = 0

    #キューが無くなるまでループ
    while dq:
        cur = dq.popleft()
        for next_node in nodes[cur]:
            if dist[next_node] != -1 : continue
            dq.append(next_node)
            dist[next_node] = dist[cur] + 1

    ans = 10**18
    for g in goal:
        if dist[g] == -1:continue
        ans = min(ans, dist[g])

    if ans == 10**18:
        print(-1)
    else:
        print(ans//2)


        


