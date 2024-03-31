S = input()
if S[0] == '<' and S[-1] == ">" and len(set(list(S[1:-1]))) == 1 and list(S[1:-1])[0] == '=':
    print('Yes')
else:
    print('No')