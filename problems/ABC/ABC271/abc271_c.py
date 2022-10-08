from collections import deque
N = int(input())
A = list(map(int,input().split()))
A.sort()
B = []
setA = set()
noneed = 0

for a in A:
    if a in setA :
        noneed += 1
        continue
    B.append(a)
    setA.add(a)

cur = 1
dq = deque(B)

while dq:
    latest = dq.popleft()
    if cur == latest:
        cur += 1
        continue
    else:
        if 2 <= noneed:
            noneed -= 2
            cur += 1
            dq.appendleft(latest)
        elif noneed == 1:
            if not dq:
                noneed -= 1
                cur += 1
                break
            else:
                dq.pop()
                noneed -= 1
                cur += 1
                dq.appendleft(latest)
        else:
            if 2 <= len(dq):
                dq.pop()
                dq.pop()
                cur += 1
                dq.appendleft(latest)
            elif 1 == len(dq):
                dq.pop()
                cur += 1
                break
            elif 0 == len(dq):
                break
    
if noneed:
    cur += noneed//2
print(cur-1)    

