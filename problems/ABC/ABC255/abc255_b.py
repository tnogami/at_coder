import math
N, K = map(int, input().split())
A = list(map(int,input().split()))
A = set(A)
akari = []
no = []

for i in range(N):
    k = i+1
    a = tuple(map(int,input().split()))
    if k in A:
        akari.append(a)
    else:
        no.append(a)


ans = 0
for n in no:
    tmp = 10**18
    for a in akari:
        d = (n[0]-a[0])**2+(n[1]-a[1])**2
        tmp = min(tmp, d)
    ans = max(ans,tmp)

print(math.sqrt(ans))
