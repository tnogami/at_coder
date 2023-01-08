S = input()
ans = len(S)

flag = False
for s in S:
    if s == '0' and flag:
        flag = False
        ans -= 1
    elif s == '0':
        flag = True
    else:
        flag = False

print(ans)