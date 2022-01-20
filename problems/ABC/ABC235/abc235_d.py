



import queue
a, N = map(int, input().split())
dist = [10**10 for i in range(N*10)] #距離
que = queue.Queue()
digit = len(str(N))

# 始点の設定
que.put(1)
dist[1] = 0


#キューが無くなるまでループ
while not que.empty():
    cur = que.get()
    
    for i in [1,2]:
        if i == 1:
            next_num = a * cur
            if digit < len(str(next_num)) : continue
            if dist[next_num] <= dist[cur] + 1 : continue
            dist[next_num] = dist[cur] + 1
            que.put(next_num)
        else:
            if len(str(cur)) == 1 or cur%10 == 0: continue
            next_num = int(str(cur)[-1] + str(cur)[:-1])
            if dist[next_num] <= dist[cur] + 1 : continue
            dist[next_num] = dist[cur] + 1
            que.put(next_num)

if dist[N] == 10**10:
    print(-1)
else:
    print(dist[N])

