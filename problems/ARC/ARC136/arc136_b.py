import copy

def check(A, B):
    flg = True
    for b in B:
        if len(A) == 3:
            break
        for i in range(len(A)):
            if A[i] == b:
                if i%2 == 0:
                    A.pop(i)
                else:
                    A.pop(i)
                    A[0], A[1] = A[1], A[0]
                break
        else:
            return False

    try_b = B[-3:]
    if A == try_b or [A[2],A[0],A[1]] == try_b or [A[1],A[2],A[0]] == try_b:
        return True
    else:
        return False

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

if check(copy.copy(A), copy.copy(B)) or check(copy.copy(B), copy.copy(A)):
    print("Yes")
else:
    print("No")
