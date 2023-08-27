import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)
N, T, M = map(int, input().split())
ng_pairs = defaultdict(set)

for _ in range(M):
    a, b = map(int, input().split())
    ng_pairs[a-1].add(b-1)
    ng_pairs[b-1].add(a-1)

ans = 0
g = [0]
size = 1


def dfs(n, g, size):
    if n == N:
        if size == T:
            global ans
            ans += 1
        return

    # iは次のgroupのindex
    for add_g_i in range(size):
        next_g = g[:]
        is_ok = True
        # 次のグループのメンバーがNGか確認
        for member, g_i in enumerate(g):
            if not add_g_i == g_i:
                continue
            if member in ng_pairs[n]:
                is_ok = False
                break

        if not is_ok:
            continue

        next_g.append(add_g_i)
        dfs(n+1, next_g, size)

    next_g = g[:]
    next_g.append(size)
    dfs(n+1, next_g, size+1)


dfs(1, g, 1)

print(ans)
