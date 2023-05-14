S = list(input())
idx_b = []
idx_r = []
idx_k = 0

for i, s in enumerate(S):
    if s == "B":
        idx_b.append(i)
    elif s == 'K':
        idx_k = i
    elif s == "R":
        idx_r.append(i)


if sum(idx_b)%2 == 1 and idx_r[0] < idx_k <idx_r[1]:
    print("Yes")
else:
    print("No")