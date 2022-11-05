def f(a,b):
    return 4*a*b+3*a+3*b

N = int(input()) 
S = list(map(int,input().split()))

A = set()

for a in range(1, 400):
    for b in range(1,400):
        A.add(f(a,b))

ans = 0
for s in S:
    if s not in A: ans += 1

print(ans)