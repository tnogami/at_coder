N = int(input())
A = list(map(int,input().split()))
A.sort()

ans = 1
limit = 10**18  
for a in A:
    ans *= a
    if ans > limit:
        print(-1)

        break
else:
    print(ans)

