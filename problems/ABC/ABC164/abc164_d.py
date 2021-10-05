S = input()
N = len(S)

mul2019 = [str(2019*i) for i in range(1, 100000)]

ans = 0
for m in mul2019:
    if m in S: ans += 1
print(ans)
