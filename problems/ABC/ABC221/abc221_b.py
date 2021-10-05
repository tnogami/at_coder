s = input()
t = input()
w = []

for i in range(len(s)):
    if s[i] != t[i]:w.append(i)

if len(w) == 0:
    print("Yes")
elif len(w) != 2:
    print("No")
else:
    if w[0] != w[1]-1:
        print("No")
    else:
        i = w[0]
        if s[i] == t[i+1] and s[i+1] == t[i]:
            print("Yes")
        else:
            print("No")
