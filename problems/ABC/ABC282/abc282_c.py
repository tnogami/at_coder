
N = int(input())
S = input()

ans = []

is_in = False

for c in S:
    if c == '"':
        is_in = not is_in
        ans.append(c)
    elif c == ',':
        if not is_in:
            ans.append('.')
        else:
            ans.append(',')
    else:
        ans.append(c)
print(''.join(ans))

