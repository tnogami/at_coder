N, K = map(int, input().split())
A = list(map(int,input().split()))

s = set()
ans = K*(K+1)//2

for a in A:
    if a <= K and a not in s:
        s.add(a)
        ans -= a

print(ans)