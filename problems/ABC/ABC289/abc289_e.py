from collections import deque
from itertools import product

def solution():
    N, M = map(int, input().split())
    A = list(map(int,input().split()))
    nodes = [[] for _ in range(N)]

    #nodeの入力
    for i in range(M):
        a,b = map(int, input().split())
        nodes[a-1].append(b-1)
        nodes[b-1].append(a-1)

    dist = [[-1]*N for _ in range(N)] #状態

    dq = deque()

    # 始点の設定
    dq.append((0, N-1))
    dist[0][N-1] = 0

    #キューが無くなるまでループ
    while dq:
        cur_taka, cur_aoki = dq.popleft()
        next_takahashi = []
        next_aoki = []
        for next_node in nodes[cur_taka]:
            next_takahashi.append(next_node)

        for next_node in nodes[cur_aoki]:
            next_aoki.append(next_node)

        for state in product(next_takahashi, next_aoki):
            taka, aoki = state
            if dist[taka][aoki] != -1 : continue
            if A[taka] == A[aoki] : continue
            dq.append(state)
            dist[taka][aoki] = dist[cur_taka][cur_aoki] + 1

    return dist[N-1][0]

T = int(input())
for _ in range(T):
    ret = solution()
    print(ret)