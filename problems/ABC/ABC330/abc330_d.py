N = int(input())
S = [input() for _ in range(N)]

ct_h = []
ct_v = []

for s in S:
    ct = 0
    for c in s:
        if c == 'o':
            ct += 1

    ct_h.append(ct)

for j in range(N):
    ct = 0
    for i in range(N):
        if S[i][j] == 'o':
            ct += 1

    ct_v.append(ct)

ans = 0
for i in range(N):
    for j in range(N):
        if S[i][j] == 'x':
            continue
        
        ans += (ct_h[i]-1)*(ct_v[j]-1)

print(ans)