import itertools
N, M = map(int, input().split())
parties = []
for _ in range(M):
    k = list(map(int,input().split()))
    s = set(k[1:])
    parties.append(s)

for a in itertools.combinations(range(N),2):
    flag = False
    for m in range(M):
        if (a[0]+1) in parties[m] and (a[1]+1) in parties[m]:
            flag = True
            break
    if not flag:
        print("No")
        break
else:
    print("Yes")