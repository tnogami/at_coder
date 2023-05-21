

N, Q = map(int, input().split())
queries = [tuple(map(int, input().split())) for _ in range(Q)]

nodes = [set() for _ in range(N)]
ans = N

for query in queries:
    if query[0] == 1:
        u, v = query[1], query[2]
        ct_u = len(nodes[u-1])
        ct_v = len(nodes[v-1])
        if ct_u == 0 and ct_v == 0:
            ans -=2
        elif ct_u == 0:
            ans -= 1
        elif ct_v == 0:
            ans -= 1
        print(ans)
        nodes[u-1].add(v-1)
        nodes[v-1].add(u-1)
    else:
        u = query[1]
        if 0 < len((nodes[u-1])):
            ans += 1
        
            for to in nodes[u-1]:
                nodes[to].remove(u-1)
                if len(nodes[to]) == 0:
                    ans += 1

            nodes[u-1] = set()

        print(ans)








