N, M = map(int, input().split())
l = 1
r = N

for i in range(M):
    L, R = map(int, input().split())
    if R<r:
        r = R
    if l<L:
        l = L

if r<l:
    print(0)
else:
    print(r-l+1)