import sys
sys.setrecursionlimit(10**9)

def dfs(n):
    global leaf_ct
    visited[n] = True
    is_leaf = True
    ret_val_max = -10**9
    ret_val_min = 10**9
    for to in nodes[n]:
        if visited[to] : continue
        is_leaf = False
        tmp = dfs(to)
        ret_val_min = min(ret_val_min, min(tmp))
        ret_val_max = max(ret_val_max, max(tmp))
    
    if is_leaf:
        ans[n] = (leaf_ct, leaf_ct)
        leaf_ct += 1
        return ans[n]
    else:
        ans[n] = (ret_val_min, ret_val_max)
        return (ret_val_min, ret_val_max)

N = int(input())
nodes = [[] for _ in range(N)]
for _ in range(N-1):
    u, v = map(int, input().split())
    nodes[u-1].append(v-1)
    nodes[v-1].append(u-1)

leaf_ct = 1
visited = [False]*N
ans = [0]*N

dfs(0)
for a in ans:
    print(*a)