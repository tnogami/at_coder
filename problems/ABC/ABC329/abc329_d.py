N, M = map(int, input().split())
A = list(map(int,input().split()))

max_ct = 0
no_1 = 10**9
n_ct = [0]*N


for a in A:
    a -= 1
    n_ct[a] += 1
    if n_ct[a] > max_ct:
        max_ct = n_ct[a]
        no_1 = a+1
        print(a+1)
    elif n_ct[a] == max_ct:
        if a+1 < no_1:
            no_1 = a+1
            print(a+1)
        else:
            print(no_1)
    else:
        print(no_1)


