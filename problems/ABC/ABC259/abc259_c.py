S = input()
T = input()

S += "#"
T += "#"

pre = ""
ct = 1
s_list = []
t_list = []
for s in S:
    if s != pre:
        s_list.append((pre, ct))
        pre = s
        ct = 1
    else:
        ct += 1

pre = ""
ct = 1
for s in T:
    if s != pre:
        t_list.append((pre, ct))
        pre = s
        ct = 1
    else:
        ct += 1

for s, t in zip(s_list[1:], t_list[1:]):

    if len(s_list) != len(t_list):
        print("No")
        break

    if s[0] != t[0]:
        print("No")
        break

    if s[1] == 1 and t[1] != 1:
        print("No")
        break

    if s[1] > t[1]:
        print("No")
        break
else:
    print("Yes")