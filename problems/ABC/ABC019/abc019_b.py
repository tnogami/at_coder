S = input()
pre = S[0]
n = 1
ans = ""
for s in S[1:]:
    if s == pre:
        n += 1
    else:
        ans += pre + str(n)
        pre = s
        n = 1

ans += s + str(n)
print(ans)



