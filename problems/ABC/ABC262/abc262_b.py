from itertools import combinations
N, M = map(int, input().split())
node = [set() for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    node[u-1].add(v-1)
    node[v-1].add(u-1)


ans = 0
for k in combinations(range(N), 3):
    if k[0] in node[k[1]] and k[1] in node[k[2]] and k[2] in node[k[0]]:
        ans += 1
print(ans)