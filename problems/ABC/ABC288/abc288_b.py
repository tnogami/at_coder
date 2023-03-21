N, K = map(int, input().split())
names = [input() for _ in range(N)]
names = names[:K]
names.sort()
for k in range(K):
    print(names[k])