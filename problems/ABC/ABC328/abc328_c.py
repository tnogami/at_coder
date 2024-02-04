N, Q = map(int, input().split())
S = list(input())

acc = [0]
cur = ""
for s in S:
    if cur == s:
        acc.append(acc[-1]+1)
    else:
        acc.append(acc[-1])
    cur = s

for _ in range(Q):
    l, r = map(int, input().split())
    print(acc[r] - acc[l])
