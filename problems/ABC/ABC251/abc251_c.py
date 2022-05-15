N = int(input())
not_origin = set()
nset = set()
hightest = 0
ans = []
for i in range(N):
    k = input().split()
    S = k[0]
    T = k[1]
    T = int(T)
    if S not in nset:
        ans.append((T, i+1))

    nset.add(S)

m = max(ans, key= lambda x:x[0])
m = m[0]
for a in ans:
    if a[0] == m:
        print(a[1])
        break

