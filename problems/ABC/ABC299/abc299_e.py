from collections import deque

N, M = map(int, input().split())
nodes = [[] for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    nodes[u].append(v)
    nodes[v].append(u)

K = int(input())
start = [tuple(map(int, input().split())) for _ in range(K)]

white_list = set()
black_list = [[] for _ in range(K)]

for i, p in enumerate(start):
    s, d = p

    dist = [-1 for i in range(N)] #距離

    dq = deque()

    # 始点の設定
    dq.append(s-1)
    dist[s-1] = 0

    #キューが無くなるまでループ
    while dq:
        cur = dq.popleft()
        if dist[cur] == d:
            black_list[i].append(cur)
            continue
        else:
            white_list.add(cur)
        
        for next_node in nodes[cur]:
            if dist[next_node] != -1 : continue
            dq.append(next_node)
            dist[next_node] = dist[cur] + 1

ans = ['0']*N
for bl in black_list:
    for idx in bl:
        if idx not in white_list:
            ans[idx] = '1'
            break
    else:
        print('No')
        break
else:
    print("Yes")
    if '1' in ans:
        print(''.join(ans))
    else:
        for i in range(N):
            if i not in white_list:
                ans[i] = '1'
                break
        print(''.join(ans))
        


