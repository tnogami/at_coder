from collections import deque
N = int(input())
A = list(map(int,input().split()))

dq = deque(A)
flip = 0
while True:
    one = flip^1
    zero = flip

    if dq[0] == one : break

    if dq[-1] == zero:
        dq.pop()
    else:
        if dq[0] == one:
            break
        else:
            dq.popleft()
            flip ^= 1

    if len(dq) == 0: break

if len(dq) == 0:
    print("Yes")
else:
    print("No")
        





