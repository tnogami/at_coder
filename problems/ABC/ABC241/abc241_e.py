N, K = map(int, input().split())
A = list(map(int,input().split()))

idx = 0
idx_list = [0]
idx_set = set([0])
num = 0
loop = False
for k in range(K):
    num += A[idx]
    idx = num%N
    if idx in idx_set: 
        loop = True
        break
    idx_list.append(idx)
    idx_set.add(idx)


if loop:
    before_loop_sum = 0
    for k in range(K):
        if idx_list[k] == idx:break
        before_loop_sum += A[idx_list[k]]
    loop_sum = 0
    loop_num = len(idx_list) - k
    before_loop = k
    for k in range(before_loop, len(idx_list)):
        loop_sum += A[idx_list[k]]

    ans = before_loop_sum
    K -= before_loop
    loop_ct = K//loop_num
    ans += loop_ct*loop_sum
    rest = K%loop_num
    for i in range(rest):
        ans += A[idx_list[before_loop+i]]
    print(ans)

else:
    print(num)



