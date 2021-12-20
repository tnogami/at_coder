S = input()
T = input()
l = set([])
for i in range(len(S)):
    l.add((ord(S[i])-ord(T[i]))%26)

if len(l) == 1:
    print("Yes")
else:
    print("No")
