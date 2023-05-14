
for j in range(8):
    S = input()
    for i, s in enumerate(S):
        if s == '*':
            ans = chr(ord('a')+i) + str(8-j)

print(ans)