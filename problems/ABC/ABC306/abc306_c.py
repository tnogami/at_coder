N = int(input())
A = list(map(int,input().split()))
d = dict()

f = []

for i, a in enumerate(A, 1):
    if a in d:
        if d[a] == 2: continue
        f.append((i, a))
        d[a] += 1
    else:
        d[a] = 1


f.sort()
ans = list(map(lambda x:x[1], f))
print(*ans)