N = int(input())
SA = []
for i in range(N):
    k = input().split()
    SA.append((k[0], int(k[1])))

idx = SA.index(min(SA, key=lambda x:x[1]))

for i in range(N):
    print(SA[idx][0])
    idx += 1
    idx %= N