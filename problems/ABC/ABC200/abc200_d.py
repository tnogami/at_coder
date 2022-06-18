N = int(input())
A = list(map(int,input().split()))
A = list(map(lambda x: x%200, A))

ans = []

for n in range(1,2**min(9,N)):

    tmp1 = []
    tmp2 = 0
    
    for i in range(min(9,N)):
        if (n>>i)&1 == 1:
            tmp1.append(i+1)
            tmp2 += A[i]

    ans.append((tmp2%200, tmp1))

ans.sort()
pre1 = -1
for s, a in ans:
    if s == pre1:
        print("Yes")
        print(len(pre2), *pre2)
        print(len(a), *a)
        break

    pre1 = s
    pre2 = a
else:
    print("No")





