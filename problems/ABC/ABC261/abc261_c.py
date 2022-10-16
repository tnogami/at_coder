N = int(input())
d = dict()
for _ in range(N):
    S = input()
    if S in d:
        print(f"{S}({d[S]})")
        d[S] += 1
    else:
        print(S)
        d[S] = 1
