import queue

N = int(input())

d = [False for i in range(N)]

waza = [list(map(int,input().split())) for i in range(N)]

que = queue.Queue()

if waza[-1][1] == 0:
    print(waza[-1][0])
else:
    for w in waza[-1][2:]:
        que.put(w-1)

    while not que.empty():
        g = que.get()
        d[g] = True
        if waza[g][1] == 0:
            continue
        else:
            for w in waza[g][2:]:
                if d[w-1] != True : que.put(w-1)

    ans = waza[-1][0]

    for i in range(N):
        if d[i] == True: ans += waza[i][0]

    print(ans)