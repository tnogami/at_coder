from collections import deque
N = int(input())
states = dict()
S = [input() for _ in range(N)]

# Pの位置を探索
idx = 0
p = [0, 0]
for i in range(N):
    for j in range(N):
        if S[i][j] == 'P':
            p[idx] = (i, j)
            idx += 1

# pの位置をイミュータブルに変換
state_key = tuple((p[0], p[1]))
states[state_key] = 0

dq = deque()
dq.append(state_key)

# 状態をBFSで探索
ans = -1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while True:
    if not dq:
        break
    state = dq.popleft()
    p1, p2 = state
    if p1 == p2:
        ans = states[state]
        break

    for i in range(4):
        np1 = (p1[0] + dx[i], p1[1] + dy[i])
        np2 = (p2[0] + dx[i], p2[1] + dy[i])
        # 壁またはfield外の場合は進めないので移動しない
        if np1[0] < 0 or np1[0] >= N or np1[1] < 0 or np1[1] >= N:
            np1 = p1
        elif S[np1[0]][np1[1]] == '#':
            np1 = p1
        if np2[0] < 0 or np2[0] >= N or np2[1] < 0 or np2[1] >= N:
            np2 = p2
        elif S[np2[0]][np2[1]] == '#':
            np2 = p2
        # すでに探索済みの場合はスキップ
        if (np1, np2) in states:
            continue
        # 未探索の場合は探索する
        states[(np1, np2)] = states[state] + 1
        dq.append((np1, np2))

print(ans)
