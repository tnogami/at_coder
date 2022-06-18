from collections import defaultdict
N, K = map(int, input().split())
A = list(map(int,input().split()))
B = A[:]
B.sort()
d = defaultdict(list)

if K == 1:
    print("Yes")
else:
    for i, a in enumerate(A):
        d[i%K].append(a)

    alist = []
    for i in range(K):
        alist.append(list(sorted(d[i])))

    num = 0
    dig = 0
    ans = []
    for i in range(len(A)):
        ans.append(alist[num][dig])
        num = (i+1)%K
        dig = (i+1)//K


    if ans == B:
        print("Yes")
    else:
        print("No")
