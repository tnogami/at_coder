N, D = map(int, input().split())
S = [input() for _ in range(N)]

ans = 0
cont = 0
for d in range(D):

    flag = True

    for n in range(N):
        if S[n][d] == 'x':
            flag = False
            break

    if flag:
        cont += 1
    else:
        cont = 0

    ans = max(ans, cont)

print(ans)
