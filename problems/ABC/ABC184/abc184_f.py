from bisect import bisect

N, T = map(int, input().split())
A = list(map(int,input().split()))
A1 = A[:N//2]
A2 = A[N//2:]

n1 = len(A1)
n2 = len(A2)

s1 = set()
s2 = set()

for n in range(2**n1):
    tmp = 0
    for i in range(n1):
        if (n >> i)&1 == 1:
            tmp += A1[i]
    s1.add(tmp)

for n in range(2**n2):
    tmp = 0
    for i in range(n2):
        if (n >> i)&1 == 1:
            tmp += A2[i]
    s2.add(tmp)

B2 = list(s2)

B2.sort()
ans = 0
for b in s1:
    target = T - b
    idx = bisect(B2, target)
    if idx == 0: continue
    ans = max(ans, b+B2[idx-1])

print(ans)

