N = int(input())
S = [input() for i in range(N)]
T = [input() for i in range(N)]

#上を削る
for i in range(N):
    if S[i] != "."*N: break
#下を削る
for ii in range(N-1, -1, -1):
    if S[ii] != "."*N: break
#左を削る
for j in range(N):
    if not all([S[k][j]=="." for k in range(N)]): break
#右を削る
for jj in range(N-1, -1, -1):
    if not all([S[k][jj]=="." for k in range(N)]): break

S_comp = []

for iii in range(i, ii+1):
    S_comp.append(S[iii][j:jj+1])

#上を削る
for i in range(N):
    if T[i] != "."*N: break
#下を削る
for ii in range(N-1, -1, -1):
    if T[ii] != "."*N: break
#左を削る
for j in range(N):
    if not all([T[k][j]=="." for k in range(N)]): break
#右を削る
for jj in range(N-1, -1, -1):
    if not all([T[k][jj]=="." for k in range(N)]): break

T_comp = []

for iii in range(i, ii+1):
    T_comp.append(T[iii][j:jj+1])

flag = False

def rot(s):
    n = len(s)
    m = len(s[0])
    ret = [[0]*n for i in range(m)]
    for i in range(m):
        for j in range(n):
            ret[i][j] = s[n-j-1][i]
    out = []
    for i in range(len(ret)):
        out.append("".join(ret[i]))
    return out

if T_comp == S_comp: flag = True

T_comp = rot(T_comp)
if T_comp == S_comp: flag = True

T_comp = rot(T_comp)
if T_comp == S_comp: flag = True

T_comp = rot(T_comp)
if T_comp == S_comp: flag = True

if flag:
    print("Yes")
else:
    print("No")