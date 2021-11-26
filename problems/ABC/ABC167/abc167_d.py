N, K = map(int, input().split())
A = list(map(int, input().split()))
visited = [1]
visited_set = set([1])
my_append = visited.append
n = A[0]
ans = -1
for i in range(1, 10**6):
    my_append(n)
    visited_set.add(n)
    n = A[n-1]
    if i == K :
        ans = visited[-1]
        break
    if n in visited_set : break

if ans == -1:
    sp = visited.index(n)
    loop = visited[sp:]
    K -= i+1
    a = K%len(loop)
    print(loop[a])
else:
    print(ans)