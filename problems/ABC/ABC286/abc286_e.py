# from collections import deque

# N = int(input())
# A = list(map(int,input().split()))
# nodes = [[] for _ in range(N)]
# for n in range(N):
#     S = input()
#     for i, s in enumerate(S):
#         if s == 'Y':
#             nodes[n].append(i)

# Q = int(input())
# for _ in range(Q):
#     U, V = map(int, input().split())
#     U -= 1
#     V -= 1

#     dist = [-1 for i in range(N)] #距離
#     price = [0 for i in range(N)]
#     dq = deque()

#     # 始点の設定
#     dq.append(U)
#     dist[U] = 0
#     price[U] = A[U]

#     #キューが無くなるまでループ
#     while dq:
#         cur = dq.popleft()
        
#         for next_node in nodes[cur]:
#             if dist[next_node] != -1 :
#                 if dist[next_node] == dist[cur] + 1:
#                     price[next_node] = max(price[next_node], price[cur]+A[next_node])
#                 continue
#             dq.append(next_node)
#             dist[next_node] = dist[cur] + 1
#             price[next_node] = price[cur] + A[next_node]


#     if price[V] == 0:
#         print('Impossible')
#     else:
#         print(dist[V],price[V])


N = int(input())
A = list(map(int,input().split()))

dist = [[float("INF")]*N for i in range(N)]
price = [[0]*N for i in range(N)]
for n in range(N):
    for m in range(N):
        price[n][m] = A[n]+A[m]

for i in range(N): #自己への移動コストはゼロ
    dist[i][i] = 0

for n in range(N):
    S = input()
    for i, s in enumerate(S):
        if s == 'Y':
            dist[n][i] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j or j == k or k == i : continue
            if dist[i][j] == dist[i][k]+dist[k][j] and dist[i][j] != float('INF'):
                price[i][j] = max(price[i][j], price[i][k]+price[k][j] - A[k])
            elif dist[i][j] < dist[i][k]+dist[k][j]:
                continue
            elif dist[i][j] > dist[i][k]+dist[k][j]:
                dist[i][j] = dist[i][k]+dist[k][j]
                price[i][j] = price[i][k]+price[k][j] - A[k]

Q = int(input())
for _ in range(Q):
    U, V = map(int, input().split())
    U -= 1
    V -= 1
    if dist[U][V] == float('INF'):
        print('Impossible')
    else:
        print(dist[U][V], price[U][V])
