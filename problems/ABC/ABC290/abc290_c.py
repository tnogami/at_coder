import collections
N, K = map(int, input().split())
A = list(map(int,input().split()))

ct = collections.Counter(A)

ans = 0
for i in range(N+1):
    if ct[i] == 0:
        break

    if ans == K:
        break
    
    ans += 1

print(ans)
