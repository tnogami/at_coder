N = int(input())
S = [input() for _ in range(N)]
ans = 10**12
for s in range(10):
    s = str(s)
    ct = 0
    tmp = 0
    t = 0
    for k in zip(*S):
        if k.count(s) == 1:
            ct += 1
            if ct == N: break
            t += 1
        elif k.count(s) == 0:
            t += 1
            continue
        else:
            ct += k.count(s)
            tmp = max(tmp, t+10*(k.count(s)-1))
            t += 1
        if ct == N:break
    
    ans = min(ans,max(tmp,t))
print(ans)




