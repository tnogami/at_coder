N, M = map(int, input().split())
S = list(input().split())
T = list(input().split())
T_set = set(T)

for s in S:
    if s in T_set:
        print("Yes")
    else:
        print("No")