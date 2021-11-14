import sys
sys.setrecursionlimit(10**9)

def dfs(n, c):
    global ans1, ans2
    visited[n] = True
    if c == 0 : 
        ans1.append(n+1)
    else:
        ans2.append(n+1)
    for to in nodes[n]:
        if visited[to]: continue
        dfs(to, (c+1)%2)

N = int(input())
nodes = [[] for i in range(N)]
visited = [False for i in range(N)]
ans1 = []
ans2 = []

for i in range(N-1):
    a, b = map(int, input().split())
    nodes[a-1].append(b-1)
    nodes[b-1].append(a-1)

dfs(0,0)

if len(ans1) < len(ans2):
    print(*ans2[:N//2])
else:
    print(*ans1[:N//2])



