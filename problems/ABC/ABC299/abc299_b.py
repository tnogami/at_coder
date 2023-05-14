N, T = map(int, input().split())
C = list(map(int,input().split()))
R = list(map(int,input().split()))

if T in C:
    pass
else:
    T = C[0]

m = 0
for i, r in enumerate(R):
    if C[i] != T: continue
    if m < r:
        ans = i+1
        m = r

print(ans)