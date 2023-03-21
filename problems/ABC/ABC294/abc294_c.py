N, M = map(int, input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = A[:]+B[:]
C.sort()
d = dict()
for i, c in enumerate(C, 1):
    d[c] = i

ans1 = []
ans2 = []

for a in A:
    ans1.append(d[a])

for a in B:
    ans2.append(d[a])

print(*ans1)
print(*ans2)
