N, M, X = map(int, input().split())
A = list(map(int,input().split()))

c1 = 0
c2 = 0
for a in A:
    if a < X: c1+=1
    if X < a: c2+=1

print(min(c1,c2))