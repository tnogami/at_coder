S = list(input())
A = list("atcoder")
ans = 0
for i, c in enumerate(A):
    if S[i] == c: continue
    
    idx = S.index(c)
    _c = S.pop(idx)
    ans += abs(i-idx)
    S = [_c] + S

print(ans)
