from collections import deque
H, W, K = map(int, input().split())
field = [input() for _ in range(H)]

ans = 10**15
# 横でK個連続させることができるか
for i in range(H):
    parts = field[i].split('x')
    for part in parts:
        if len(part) < K:
            continue

        ct_maru = 0
        dq = deque()
        for k in range(K):
            if part[k] == 'o':
                ct_maru += 1
            dq.append(part[k])

        tmp_ans = K - ct_maru        
        for k in range(len(part)-K):
            s = dq.popleft()
            if s == 'o':
                ct_maru -= 1
            if part[k+K] == 'o':
                ct_maru += 1
            tmp_ans = min(tmp_ans, K - ct_maru)

        ans = min(ans, tmp_ans)

# 行列を入れ替えて、縦でK個連続させることができるか
W, H = H, W
field = list(zip(*field))
field = [''.join(f) for f in field]
for i in range(H):
    parts = field[i].split('x')
    for part in parts:
        if len(part) < K:
            continue

        ct_maru = 0
        dq = deque()
        for k in range(K):
            if part[k] == 'o':
                ct_maru += 1
            dq.append(part[k])

        tmp_ans = K - ct_maru        
        for k in range(len(part)-K):
            s = dq.popleft()
            if s == 'o':
                ct_maru -= 1
            if part[k+K] == 'o':
                ct_maru += 1
            tmp_ans = min(tmp_ans, K - ct_maru)

        ans = min(ans, tmp_ans)

if ans == 10**15:
    print(-1)
else:
    print(ans)