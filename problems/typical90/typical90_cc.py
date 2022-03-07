def dim2imos(A:list) -> list:
    from itertools import accumulate
    ret = []
    for a in A:
        ret.append(list(accumulate(a)))
    for i in range(len(ret)-1):
        ret[i+1] = [ret[i][j]+ret[i+1][j] for j in range(len(ret[i]))]
    return ret

acc = [[0]*(5002) for _ in range(5002)]

N, K = map(int, input().split())

for _ in range(N):
    A, B = map(int, input().split())
    acc[A][B] += 1

acc = dim2imos(acc)

ans = 0
for a in range(1,5001):
    for b in range(1,5001):
        ar = min(a+K, 5000)
        br = min(b+K, 5000)
        tmp = acc[ar][br] - acc[ar][b-1] - acc[a-1][br] + acc[a-1][b-1]
        ans = max(ans, tmp)

print(ans)

    