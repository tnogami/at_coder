
N, Q = map(int, input().split())

pos_histry = [(i+1, 0) for i in range(N)][::-1]
cur_pos = (1, 0)
for _ in range(Q):
    t, q = input().split()
    if t == '1':
        if q == 'U':
            cur_pos = (cur_pos[0], cur_pos[1]+1)
        elif q == 'D':
            cur_pos = (cur_pos[0], cur_pos[1]-1)
        elif q == 'L':
            cur_pos = (cur_pos[0]-1, cur_pos[1])
        elif q == 'R':
            cur_pos = (cur_pos[0]+1, cur_pos[1])
        pos_histry.append(cur_pos)
    else:
        print(*pos_histry[-(int(q))])

