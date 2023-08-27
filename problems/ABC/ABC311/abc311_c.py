N = int(input())
A = list(map(int, input().split()))

visited = [False]*N

cur = 0
visited[cur] = True

while True:
    next_node = A[cur]-1
    if visited[next_node]:
        break

    visited[next_node] = True
    cur = next_node


visited = [False]*N

cur = next_node
visited[cur] = True
ans = [cur+1]

while True:
    next_node = A[cur]-1
    if visited[next_node]:
        break

    visited[next_node] = True
    cur = next_node
    ans.append(cur+1)

print(len(ans))
print(*ans)
