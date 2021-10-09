import queue

N = int(input())
dist = [-1 for i in range(N)] #距離
que = queue.Queue()
nodes = [[] for i in range(N)]

#nodeの入力
for i in range(N-1):
    a,b = map(int, input().split())
    nodes[a-1].append(b-1)
    nodes[b-1].append(a-1)

# 始点の設定
que.put(0)
dist[0] = 0

#キューが無くなるまでループ
while not que.empty():
    cur = que.get()
    
    for next_node in nodes[cur]:
        if dist[next_node] != -1 : continue
        que.put(next_node)
        dist[next_node] = dist[cur] + 1

st = dist.index(max(dist))

dist = [-1 for i in range(N)] #距離の初期化
que.put(st)
dist[st] = 0

while not que.empty():
    cur = que.get()
    
    for next_node in nodes[cur]:
        if dist[next_node] != -1 : continue
        que.put(next_node)
        dist[next_node] = dist[cur] + 1

print(max(dist)+1)