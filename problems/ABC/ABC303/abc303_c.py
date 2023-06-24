N, M, H, K = map(int, input().split())

S = input()

xy = set([tuple(map(int, input().split())) for _ in range(M)])
used = set()

pos = [0, 0]

num = 0
ans = False
for s in S:
    H -= 1
    num += 1

    if H < 0:
        break

    if num == N:
        ans = True
        break

    if s == 'U':
        pos[1] += 1
    elif s == 'D':
        pos[1] -= 1
    elif s == 'L':
        pos[0] -= 1
    elif s == 'R':
        pos[0] += 1

    if H < K:
        if tuple(pos) in xy and tuple(pos) not in used:
            H = K
            used.add(tuple(pos))


if ans:
    print("Yes")
else:
    print("No")
