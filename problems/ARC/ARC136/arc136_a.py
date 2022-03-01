N = int(input())
S = input()
tmp = []

for s in S:
    if s == "A":
        tmp.append("B")
        tmp.append("B")
    else:
        tmp.append(s)

ans = []

ct_b = 0
for t in tmp:
    if t == "B":
        if ct_b == 1:
            ans.append("A")
            ct_b = 0
        else:
            ct_b = 1
    else:
        if ct_b == 1:
            ans.append("B")
            ans.append(t)
            ct_b = 0
        else:
            ans.append(t)

if ct_b == 1:ans.append("B")
print("".join(ans))
