# import bisect
# def f(a,b):
#     return a**3+a**2*b+a*b**2+b**3

# N = int(input())

# ans = [0]
# for a in range(10**6+1):
#     ok = 10**6+1
#     ng = 0
#     while 1 < ok-ng:
#         m = (ok+ng)//2
#         if f(a,m) < N:
#             ng = m
#         else:
#             ok = m
#     ans.append(f(a,ok))

# ans.sort()
# idx = bisect.bisect_left(ans,N)
# print(ans[idx])

#別解

import bisect
def f(a,b):
    return a**3+a**2*b+a*b**2+b**3

N = int(input())

x = 10**19
j = 10**6
for i in range(10**6+1):
    while(f(i,j)>=N and j>=0):
        x=min(x,f(i,j))
        j -= 1
print(x)