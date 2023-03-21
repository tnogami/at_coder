from heapq import heappop, heappush

N, M = map(int, input().split())

out_list = [set() for _ in range(N)]
in_list = [set() for _ in range(N)]
inc = [0]*N
XY = set([tuple(map(int, input().split())) for _ in range(M)])
for x, y in XY:
    x -= 1
    y -= 1
    out_list[x].add(y)
    in_list[y].add(x)
    inc[y] += 1

S = []
L1 = [] 
inc1 = inc[:]
for i, c in enumerate(inc1):
    if c == 0:
        heappush(S, i)

while S:
    n = heappop(S)
    L1.append(n)
    for m in out_list[n]:
        inc1[m] -= 1
        if inc1[m] == 0:
            heappush(S, m)
#============================

S = []
L2 = [] 
inc2 = inc[:]
for i, c in enumerate(inc2):
    if c == 0:
        heappush(S, -i)
while S:
    n = heappop(S)
    n *= -1
    L2.append(n)
    for m in out_list[n]:
        inc2[m] -= 1
        if inc2[m] == 0:
            heappush(S, -m)

if L1 == L2:
    print("Yes")
    output = [0]*N
    for i, a in enumerate(L1):
        output[a] = i+1
    print(*output)
else:
    print("No")


# # 入次数0を探索
# ct = 0
# target = -1
# for i, c in enumerate(in_list):
#     if len(c) == 0:
#         ct += 1
#         target = i

# ans = [target+1]
# total = 1
# flag = True

# if ct != 1:
#     print("No")
# else:
#     while True:
#         if total == N:
#             break

#         ct = 0
#         for out in out_list[target]:
#             in_list[out].remove(target)
#             if len(in_list[out]) == 0:
#                 ct += 1
#                 next_target = out
            
#         if ct != 1:
#             flag = False
#             break
        
#         target = next_target
#         ans.append(target+1)
#         total += 1

#     if flag:
#         print("Yes")
#         output = [0]*N
#         for i, a in enumerate(ans):
#             output[a-1] = i+1
#         print(*output)
#     else:
#         print("No")

