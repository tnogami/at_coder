N = int(input())
edges = dict()
starts = set()

for _ in range(N):
    S, T = input().split()
    edges[S] = T
    starts.add(S)


is_impossible = False

visited = set()

for node in starts:
    if node in visited: continue

    cur_visited = set([node])
    
    while True:
        if node not in starts:
            break
        next_node = edges[node]
        if next_node in cur_visited:
            is_impossible = True
            break
        else:
            node = next_node
            cur_visited.add(node)

    visited |= cur_visited
    if is_impossible: break

if is_impossible:
    print("No")
else:
    print("Yes")
