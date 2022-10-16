
masu = [0] * 1000
LR = list(map(int,input().split()))
for i in range(LR[0], LR[1]):
    masu[i] += 1
for i in range(LR[2], LR[3]):
    masu[i] += 1

print(masu.count(2))

