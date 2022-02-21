import copy
N = int(input())
A = list(map(int,input().split()))

ans = []
cur = [-1,0]
ct = 0
m = 0
for i,a in enumerate(A):
    if a == cur[0]:
        if cur[1]+1 == cur[0]:
            m += cur[0]
            if ans:
                cur = ans.pop()
            else:
                cur = [-1,0]
        else:
            cur[1] += 1
    else:
        ans.append(copy.copy(cur))
        cur[0] = a
        cur[1] = 1
        
    print(i+1-m)
