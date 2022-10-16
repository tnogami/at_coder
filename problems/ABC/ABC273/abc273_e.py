Q = int(input())
ans = []
pages_node = dict()
pages_parent = dict()
pages_cursor = dict()
queries = [input().split() for _ in range(Q)]

parent = [-1]
nodes = [-1]
cursor = 0
for query in queries:
    command = query[0]

    if command == "ADD":
        nodes.append(query[1])
        parent.append(cursor)
        cursor = len(nodes) - 1
    elif command == "DELETE":
        if cursor == 0:
            pass
        else:
            cursor = parent[cursor]
    elif command == "SAVE":
        pages_node[query[1]] = nodes
        pages_parent[query[1]] = parent
        pages_cursor[query[1]] = cursor
    elif command == "LOAD":
        if query[1] in pages_node:
            nodes = pages_node[query[1]]
            parent = pages_parent[query[1]]
            cursor = pages_cursor[query[1]]
        else:
            parent = [-1]
            nodes = [-1]
            cursor = 0
    ans.append(nodes[cursor])


print(*ans)

