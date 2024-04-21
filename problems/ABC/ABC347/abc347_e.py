N, Q = map(int, input().split())
X = list(map(int,input().split()))
ans = [0] * N
S = set()

acc_lenS = [0]

starts_num = [0] * N

for i, x in enumerate(X):
    if x in S:
        S.remove(x)
        ans[x - 1] += acc_lenS[-1] - acc_lenS[starts_num[x - 1]]
        acc_lenS.append(acc_lenS[-1] + len(S))
    else:
        S.add(x)
        acc_lenS.append(acc_lenS[-1] + len(S))
        starts_num[x - 1] = i
for s in S:
    ans[s - 1] += acc_lenS[-1] - acc_lenS[starts_num[s - 1]]

print(*ans)