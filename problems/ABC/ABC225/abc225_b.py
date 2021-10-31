N = int(input())
nodes = [[] for i in range(N)]

for i in range(N-1):
    a, b = map(int, input().split())
    nodes[a-1].append(b-1)
    nodes[b-1].append(a-1)

for i in range(N):
    if len(nodes[i]) == N-1:
        print("Yes")
        break
else:
    print("No")


