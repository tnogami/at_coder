N = int(input())
A = list(map(int,input().split()))

same = 0
same_list = dict()
ans = 0
for i, a in enumerate(A):
    if a == i+1:
        ans += same
        if a in same_list:
            ans -= same_list[a]
            same_list[a] += 1
        else:
            same_list[a] = 1
        same += 1
    else:
        if A[a-1] == i+1 and a-1 < i : ans += 1

print(ans)


