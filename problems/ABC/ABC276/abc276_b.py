N, M = map(int, input().split())
nodes = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    nodes[a-1].append(b)
    nodes[b-1].append(a)

for node in nodes:
    num = len(node)
    node.sort()
    print(num, *node)