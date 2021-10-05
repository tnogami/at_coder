N = int(input())
A = list(map(int,input().split()))
if sum(A)%N != 0:
    print(-1)
else:
    req = sum(A)//N
    people = 0
    island = 0
    ans = 0
    for a in A:
        island += 1
        people += a
        if island*req != people:ans+=1
    print(ans)