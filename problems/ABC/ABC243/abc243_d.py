N, X = map(int, input().split())
S = input()
u_ct = 0
r_ct = 0
l_ct = 0

stack = []

for s in S:
    if not stack:
        stack.append(s)
    else:
        if s == "U":
            if stack[-1] != "U":
                stack.pop()
            else:
                stack.append(s)
        else:
            stack.append(s)
 
for s in stack:
    if s == "U":
        X //= 2
    elif s == "L":
        X *= 2
    else:
        X *= 2
        X += 1

print(X)