from collections import deque

Q = int(input())
q1 = deque()
q2 = deque()

for _ in range(Q):
    q = list(map(int,input().split()))    
    if q[0] == 1:
        q1.append([q[1],q[2]])
    else:
        q2.append(q[1])


while q2:
    c2 = q2.popleft()
    ct = 0
    s = 0
    while True:
        x, c1 = q1.popleft()
        if c2 < ct + c1:
            c1 -= c2 - ct
            s += x * (c2 - ct)
            q1.appendleft([x,c1])
            break
        else:
            ct += c1
            s += x * c1
        if ct == c2 : break
    print(s)

