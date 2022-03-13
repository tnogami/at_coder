# import copy

# def restore_path(start,end):
#     global ans
#     cur = start
#     while (cur != end):
#         for i in range(N):
#             if i != cur and dist_old[cur][i] + dist[i][end] == dist[cur][end]:
#                 ans.add((min(cur,i),max(cur,i)))
#                 cur = i
#                 break

N, M = map(int, input().split())

dist = [[10**15]*N for i in range(N)]
edges = []
    
for i in range(M):
    a,b,t = map(int, input().split())
    dist[a-1][b-1] = t
    dist[b-1][a-1] = t
    edges.append((a-1, b-1, t))

# dist_old = copy.deepcopy(dist)
#ワーシャル・フロイド法でi-jの最小コストを計算
for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])



# ans = set()

# for st in range(N-1):
#     for gl in range(st+1, N):
#         restore_path(st, gl)

ans = 0
for a, b, t in edges:
    for middle in range(N):
        if middle == a or middle == b : continue
        if dist[a][middle]+dist[middle][b] <= t:
            ans += 1
            break

print(ans)
