S = input()
ans = [0 for i in range(len(S))]
S += "R"

r_num = 0
l_num = 0
sw_flag = False

for i, s in enumerate(S):
    if s == "L" :
        if l_num == 0:
            idx = i
        l_num += 1
    else:
        if l_num == 0:
            r_num += 1
        else:
            ans[idx] = r_num//2 + l_num - (l_num//2)
            ans[idx-1] = r_num - (r_num//2) + l_num//2
            l_num = 0
            r_num = 1

print(" ".join(list(map(str, ans))))
