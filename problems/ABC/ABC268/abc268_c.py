import collections
N = int(input())
P = list(map(int,input().split())) 
ct = collections.Counter()
for i, p in enumerate(P):
    if i <= p:
        ct[p-i] += 1
        ct[p-i+1] += 1
        if p-i-1 < 0:
            ct[(p-i-1)+N] += 1
        else:
            ct[p-i-1] += 1
            
    else:
        ct[N+p-i] += 1
        ct[N+p-i+1] += 1
        ct[N+p-i-1] += 1

print(max(ct.values()))

