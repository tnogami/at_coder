HEAD = 0
TAIL = 1

N, Q = map(int, input().split())

trains = [[-1, -1] for i in range(N)]

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        trains[q[1]-1][TAIL] = q[2]-1 
        trains[q[2]-1][HEAD] = q[1]-1
    elif q[0] == 2:
        trains[q[1]-1][TAIL] = -1
        trains[q[2]-1][HEAD] = -1
    else:
        h = []
        next_head = trains[q[1]-1][HEAD]
        while next_head != -1:
            h.append(str(next_head+1))
            next_head = trains[next_head][HEAD]
        t = []
        next_tail = trains[q[1]-1][TAIL]
        while next_tail != -1:
            t.append(str(next_tail+1))
            next_tail = trains[next_tail][TAIL]
        ans = h[::-1] + [str(q[1])] + t
        ans = [str(len(ans))] + ans
        print(" ".join(ans))


