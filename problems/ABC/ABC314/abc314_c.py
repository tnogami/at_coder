from collections import deque
N, M = map(int, input().split())
S = input()
C = list(map(int, input().split()))

dqs = [deque([]) for _ in range(M)]

for color, chara in zip(C, S):
    dqs[color-1].append(chara)

for m in range(M):
    p = dqs[m].pop()
    dqs[m].appendleft(p)

ans = []

for c in C:
    ans.append(dqs[c-1].popleft())

print(''.join(ans))
