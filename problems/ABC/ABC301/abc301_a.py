N = int(input())
S = input()

tc = 0
ac = 0

for s in S:
    if s =='A':
        ac += 1
    else:
        tc += 1

if ac == tc:
    if S[-1] == 'T':
        print('A')
    else:
        print('T')
elif ac < tc:
    print('T')
else:
    print('A')