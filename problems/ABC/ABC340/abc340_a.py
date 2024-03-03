A, B, D = map(int, input().split())

ans = []

while True:
    ans.append(A)
    A += D
    if ans[-1] == B:
        break

print(*ans)