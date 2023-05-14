def check(C, D):
    ans = True
    for c, d in zip(C,D):
        if c != d:
            ans = False
            break
    return ans

def trans_h(E):
    q = E.popleft()
    E.append(q)
    return E

def trans_v(E):
    for h in range(H):
        e = E[h].popleft()
        E[h].append(e)

    return E

from collections import deque

H, W = map(int, input().split())
A = deque([deque(list(input())) for _ in range(H)])

B = deque([deque(list(input())) for _ in range(H)])

ans = False
for h in range(H+1):
    A = trans_h(A)
    for v in range(W+1):
        A = trans_v(A)
        if check(A,B):ans = True

if ans :
    print("Yes")
else:
    print("No")
