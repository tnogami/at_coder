N = int(input())
A = list(map(int,input().split()))

masu = [0,0,0,0]

ans = 0
for i in range(N):
    if A[i] == 1:
        ans += masu[3]
        masu3 = masu[3]
        masu2 = masu[2]
        masu1 = masu[1]
        masu[0] = 0
        masu[1] = 1
        masu[2] = masu1
        masu[3] = masu2
    elif A[i] == 2:
        ans += masu[3]
        ans += masu[2]
        masu3 = masu[3]
        masu2 = masu[2]
        masu1 = masu[1]
        masu[0] = 0
        masu[1] = 0
        masu[2] = 1
        masu[3] = masu1
    elif A[i] == 3:
        ans += masu[3]
        ans += masu[2]
        ans += masu[1]
        masu3 = masu[3]
        masu2 = masu[2]
        masu1 = masu[1]
        masu[0] = 0
        masu[1] = 0
        masu[2] = 0
        masu[3] = 1
    else:
        ans += masu[3]
        ans += masu[2]
        ans += masu[1]
        ans += 1
        masu3 = masu[3]
        masu2 = masu[2]
        masu1 = masu[1]
        masu[0] = 0
        masu[1] = 0
        masu[2] = 0
        masu[3] = 0

print(ans)