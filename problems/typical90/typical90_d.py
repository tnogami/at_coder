H, W = map(int, input().split())
A = [list(map(int,input().split())) for i in range(H)]
A_t = [list(x) for x in zip(*A)]

H_sum = []
W_sum = []

for i in range(H):
    H_sum.append(sum(A[i]))

for i in range(W):
    W_sum.append(sum(A_t[i]))

for i in range(H):
    ans = []
    for j in range(W):
        ans.append(str(H_sum[i]+W_sum[j]-A[i][j]))
    print(" ".join(ans))