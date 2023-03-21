N = int(input())
S = input()
pos = set([(0,0)])
cur = [0,0]
for s in S:
    if s == 'R':
        cur[0] += 1
    elif s == 'L':
        cur[0] -= 1
    elif s == 'U':
        cur[1] += 1
    elif s == 'D':
        cur[1] -= 1

    t_cur = tuple(cur)

    if t_cur in pos:
        print("Yes")
        break
    else:
        pos.add(t_cur)
else:
    print("No")

