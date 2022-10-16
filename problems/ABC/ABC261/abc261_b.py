N = int(input())
A = [input() for _ in range(N)]
flag = True
for i in range(N-1):
    for j in range(i+1, N):
        if A[i][j] == 'W':
            if A[j][i] == 'L': continue
            flag = False
        elif A[i][j] == 'L':
            if A[j][i] == 'W': continue
            flag = False
        elif A[i][j] == 'D':
            if A[j][i] == 'D': continue
            flag = False

if flag:
    print('correct')
else:
    print('incorrect')