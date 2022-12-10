H, W = map(int, input().split())
S = [input() for _ in range(H)]
T = [input() for _ in range(H)]
new_S = list(map(lambda x:"".join(x), [list(x) for x in zip(*S)]))
new_T = list(map(lambda x:"".join(x), [list(x) for x in zip(*T)]))
new_S.sort()
new_T.sort()

if new_S == new_T:
    print("Yes")
else:
    print("No")