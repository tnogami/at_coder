H, W, K = map(int, input().split())
S = [tuple(map(int, input())) for _ in range(H)]
ans = 10**12

for n in range(2**(H-1)):
    groups = [[0]]
    for i in range(H-1):
        if (n>>i)&1 == 1:
            groups.append([i+1])
        else:
            groups[-1].append(i+1)

    ct = [0]*len(groups)
    tmp_ct = [0 for _ in range(len(groups))]

    tmp = 0

    fault_flg = False
    for i in range(W):
        tmp_ct = [0]*len(groups)
        for k, group in enumerate(groups):
            for g in group:
                tmp_ct[k] += S[g][i]
            if K < tmp_ct[k]:
                fault_flg = True
                break
        else:
            for k in range(len(groups)):
                ct[k] += tmp_ct[k]
            for c in ct:
                if K < c:
                    tmp += 1
                    ct = tmp_ct
                    break

        if fault_flg:
            tmp = 10**12
            break
    else:
        tmp += len(groups) - 1

    ans = min(ans,tmp)


print(ans)


