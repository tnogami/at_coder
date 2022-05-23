N, X = map(int, input().split())
M = [i+1 for i in range(N)]
M.pop(X-1)
ans = []
mid_idx = N//2 - 1
if N%2 == 0:
    if N//2 < X:
        plus = True
    else:
        plus = False
else:
    plus = True
idx = mid_idx
add = 1
ans.append(M[mid_idx])
for i in range(N-2):
    if plus:
        idx += add
    else:
        idx -= add
    ans.append(M[idx])
    add += 1
    plus ^= True

ans = [X]+ans
print(*ans)

