N = int(input())

A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

def rot(S):
    T_S = list(zip(*S))
    ret = []
    for x in T_S[::-1]:
        ret.append(x)
    return ret

def check(A, B):
    flag = True
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1 and B[i][j] == 0:
                flag = False

    return flag

is_ok = False
for _ in range(4):
    A = rot(A)
    is_ok = is_ok or check(A, B)
    
if is_ok:
    print('Yes')
else:
    print('No')
    