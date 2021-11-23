S, T, X = map(int, input().split())

ans = []
for i in range(100):
    ans.append(S)
    S += 1
    S %= 24
    if S == T:
        break

if X in ans:
    print("Yes")
else:
    print("No")


