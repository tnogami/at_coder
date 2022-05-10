from collections import defaultdict
H, W, M = map(int, input().split())
targets = [tuple(map(int,input().split())) for _ in range(M)]
targets_set = set(targets)

w_ct = defaultdict(int)
h_ct = defaultdict(int)
for target in targets:
    h, w = target
    w_ct[w] += 1
    h_ct[h] += 1

max_w = max(w_ct.values())
max_h = max(h_ct.values())

max_w_list = [k for k,v in w_ct.items() if v == max_w]
max_h_list = [k for k,v in h_ct.items() if v == max_h]

flag = False
for w in max_w_list:
    for h in max_h_list:
        if (h,w) not in targets_set:
            flag = True
            break
    if flag : break

if flag :
    print(max_h+max_w)
else:
    print(max_w+max_h-1)



