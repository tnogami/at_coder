N = int(input())
A = list(map(int,input().split()))
A.sort(reverse = True)

num = A[0]
e = 0
ans = 1
for a in A[1:]:
    if a == num:
        e += 1
        ans *= num
        num = -1
    else:
        num = a

    if e == 2:
        print(ans)
        break
else:
    print(0)



