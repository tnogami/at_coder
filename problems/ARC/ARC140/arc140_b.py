from collections import defaultdict
N = int(input())
S = list(input())
S.append("A")

stack = []
comb = 0
trans = defaultdict(int)

for c in S:
    if c != "C":
        stack.append(c)
        if comb: trans[comb] += 1
        comb = 0
        continue

    if len(stack) < 2 :
        stack = []
        if comb: trans[comb] += 1
        comb = 0
        continue

    if stack[-1] != "R" or stack[-2] != "A":
        stack = []
        if comb: trans[comb] += 1
        comb = 0
        continue

    r = stack.pop()
    a = stack.pop()
    stack.append("R")
    comb += 1

oe = 0
if not trans:
    print(0)
else:
    ans = 0
    while True:
        if oe == 0:
            m = max(trans.keys())
            trans[m] -= 1
            if trans[m] == 0: del trans[m]
            if m != 1:
                trans[m-1] += 1
            ans += 1
        else:
            m = min(trans.keys())
            trans[m] -= 1
            if trans[m] == 0: del trans[m]
            ans += 1
        oe ^= 1
        if not trans : break

    print(ans)
