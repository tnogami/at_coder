N, K = map(int, input().split())
C = list(map(int,input().split()))

d = dict()

for i in range(K):
    color = C[i]
    if color in d:
        d[color] += 1
    else:
        d[color] = 1

ans = len(d)

for i in range(K,N):
    add_color = C[i]
    if add_color in d:
        d[add_color] += 1
    else:
        d[add_color] = 1

    del_color = C[i-K]
    d[del_color] -= 1
    if d[del_color] == 0:del d[del_color]

    ans = max(ans, len(d))

print(ans)



