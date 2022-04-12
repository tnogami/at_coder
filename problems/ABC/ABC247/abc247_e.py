from collections import deque

N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
A.append(X+1)

div_A = []
tmp = []
for a in A:
    if Y <= a <= X:
        tmp.append(a)
    else:
        if tmp:
            div_A.append(tmp)
            tmp = []
            
ans = 0
for a in div_A:
    length = len(a)
    dq = deque()
    ct = [0,0]
    for i, c in enumerate(a):
        dq.append((i,c))
        if c == X:
            ct[0] += 1
        if c == Y:
            ct[1] += 1
        
        while dq and 1 <= ct[0] and 1 <= ct[1]:
            idx, rm = dq.popleft()
            ans += length - i
            if rm == X:
                ct[0] -= 1
            if rm == Y:
                ct[1] -= 1
                
print(ans)