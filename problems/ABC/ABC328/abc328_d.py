from collections import deque
S = input()

dq = deque()

cur_status = 0

ans = []
for s in list(S):
    dq.append(s)
    if s == 'A':
        cur_status = 1
    elif s == 'B':
        if cur_status == 1:
            cur_status = 2
        else:
            cur_status = 0
    elif s == 'C':
        if cur_status == 2:
            for _ in range(3):
                dq.pop()
        
        if dq and dq[-1] == 'A':
            cur_status = 1
        elif len(dq)>1 and dq[-1] == 'B' and dq[-2] == 'A':
            cur_status = 2
        else:
            cur_status = 0

print(''.join(dq))



