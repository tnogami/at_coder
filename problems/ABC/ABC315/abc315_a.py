S = input()
ans = []

for s in S:
    if s in ['a', 'i', 'u', 'e', 'o']:
        continue
    else:
        ans.append(s)

print(''.join(ans))
