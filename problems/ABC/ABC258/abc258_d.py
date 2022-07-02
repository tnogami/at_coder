from itertools import accumulate

N, X = map(int, input().split())
AB = [list(map(int,input().split())) for _ in range(N)]

sum_AB = list(map(sum, AB))

acc = list(accumulate(sum_AB))


ans = 10**21
for n in range(N):
    tmp = 0
    if X < n+1 :break
    tmp += acc[n]
    tmp += AB[n][1]*(X-n-1)
    ans = min(ans,tmp)

print(ans)