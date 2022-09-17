lines = {0:[6], 1:[3], 2:[1,7], 3:[0,4], 4:[2,8], 5:[5], 6:[9]}
S = input()
if S[0] == "1":
    print("No")
else:
    for i in range(5):
        for j in range(i+2, 7):
            ct_i = 0
            ct_j = 0
            for _i in lines[i]:
                ct_i += int(S[_i])
            for _j in lines[j]:
                ct_j += int(S[_j])
            if 0 < ct_i and 0 < ct_j:
                ct_k = 0
                for k in range(i+1, j):
                    for _k in lines[k]:
                        ct_k += int(S[_k])
                if ct_k == 0:
                    print("Yes")
                    exit()
    else:
        print("No")

