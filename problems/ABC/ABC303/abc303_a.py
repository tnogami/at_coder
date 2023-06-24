N = int(input())
S = input()
T = input()

ans = True

for s, t in zip(S, T):
    s = s.replace('0', 'o').replace('1', 'l')
    t = t.replace('0', 'o').replace('1', 'l')
    if s == t : continue
    ans = False

if ans :
    print("Yes")
else:
    print("No")