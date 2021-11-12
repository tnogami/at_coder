import sys
sys.setrecursionlimit(10**9)
MOD = 998244353

def dfs(n):
    visited[n] = True
    v = 1
    e = 0
    for to in nodes[n]:
        e += 1
        if visited[to] == True: continue
        tmp_e, tmp_v = dfs(to)
        v += tmp_v
        e += tmp_e
        
    return e, v

N, M = map(int, input().split())
nodes = [[] for i in range(N)]
for i in range(M):
    u, v = map(int, input().split())
    nodes[u-1].append(v-1)
    nodes[v-1].append(u-1)
    
visited = [False for i in range(N)]
    
ans = 1
for i in range(N):
    if visited[i] == True:continue
    ec, vc = dfs(i)
    if ec//2 == vc :
        ans *= 2
        ans %= MOD
    else:
        ans *= 0
    
print(ans)
    
    