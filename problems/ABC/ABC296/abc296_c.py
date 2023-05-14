N, X = map(int, input().split())
A = list(map(int,input().split()))

s = set()

for a in A:
    req1 = X + a
    req2 = a - X
    s.add(a)
    if req1 in s or req2 in s:
        print("Yes")
        break
else:
    print("No")

