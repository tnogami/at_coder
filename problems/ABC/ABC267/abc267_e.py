N, M = map(int, input().split())
A = list(map(int,input().split()))
nodes = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    nodes[a-1].append(b-1)




