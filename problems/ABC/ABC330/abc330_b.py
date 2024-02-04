N, L, R = map(int, input().split())
A = list(map(int, input().split()))

ans = []
for a in A:
    # abs(a-X)を最小にするXをL<=X<=Rの範囲で求める
    if a < L:
        X = L
    elif a > R:
        X = R
    else:
        X = a
    ans.append(X)

print(*ans)
