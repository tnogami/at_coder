N = int(input())
B = bin(N)[2:]
L = []
ct = 0

for i, b in enumerate(B[::-1]):
    if b == "1":
        L.append(i)
        ct += 1

ans = []
for n in range(2**ct):
    tmp = 0
    for j in range(ct):
        if ((n >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う1
            tmp = tmp|(1<<L[j])
    ans.append(tmp)

ans.sort()
for a in ans:
    print(a)


