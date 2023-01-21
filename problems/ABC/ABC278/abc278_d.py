N = int(input())
A = list(map(int,input().split()))
Q = int(input())

one_add = dict()
all_in = -1
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        all_in = query[1]
        one_add = dict()
    elif query[0] == 2:
        if query[1]-1 in one_add:
            one_add[query[1]-1] += query[2]
        else:
            one_add[query[1]-1] = query[2]
    else:
        if all_in == -1:
            if query[1]-1 in one_add:
                print(A[query[1]-1] + one_add[query[1]-1])
            else:
                print(A[query[1]-1])
        else:
            if query[1]-1 in one_add:
                print(all_in + one_add[query[1]-1])
            else:
                print(all_in)
