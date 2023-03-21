from itertools import combinations
H, W = map(int, input().split())
A = [list(map(int,input().split())) for _ in range(H)]

options = list(range(H+W-2))
ans = 0

for go_right in combinations(options, W-1):
    go_right = set(go_right)

    cur = [0, 0]
    nums = set([A[0][0]])

    for i in range(H+W-2):
        if i in go_right:
            cur[1] += 1
        else:
            cur[0] += 1

        if A[cur[0]][cur[1]] in nums:
            break
        else:
            nums.add(A[cur[0]][cur[1]])
    else:
        ans += 1

print(ans)
