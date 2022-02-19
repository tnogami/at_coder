import sys
sys.setrecursionlimit(10**9)

def dfs(i):
    visited[i] = True
    
    s = [X[i]]
    for j in nodes[i]:
        if visited[j] : continue
        s.extend(dfs(j))
    s.sort(reverse=True)
    tmp = []
    for k, _s in enumerate(s):
        tmp.append(_s)
        if k == 19:break
    ans[i].extend(tmp)
    return tmp

N, Q = map(int, input().split())
X = list(map(int,input().split()))

nodes = [[] for i in range(N)]
ans = [[] for i in range(N)]
visited = [False]*N

for _ in range(N-1):
   a, b = map(int, input().split())
   nodes[b-1].append(a-1)
   nodes[a-1].append(b-1)

dfs(0)

for _ in range(Q):
    v, k = map(int, input().split())
    print(ans[v-1][k-1])
