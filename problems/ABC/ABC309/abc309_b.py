import copy
N = int(input())
A = [list(input()) for _ in range(N)]
ans = copy.deepcopy(A)

ans[0] = [A[1][0]] + A[0][:-1]
ans[-1] = A[-1][1:] + [A[-2][-1]]

for i in range(1, N-1):
    ans[i][0] = A[i+1][0]
    ans[i][-1] = A[i-1][-1]

for a in ans:
    print(''.join(a))
