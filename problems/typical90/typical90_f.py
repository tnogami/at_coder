from collections import deque
N, K = map(int, input().split())
S = input()
d = dict()

for i, c in enumerate(S):
    if c in d:
        d[c].append(i)
    else:
        d[c] = deque([i])

l = []
for key, val in d.items():
    l.append({"char":key, "que":val})

l.sort(key=lambda x:x["char"])

req_num = K
ans = []
last_idx = -1
while req_num != 0:
    for i in range(len(l)):
        idx = l[i]["que"].popleft()
        if N-idx-1 < req_num - 1:
            l[i]["que"].appendleft(idx)
            continue
        else:
            if last_idx < idx:
                ans.append(l[i]["char"])
                last_idx = idx
                req_num -= 1
            if not l[i]["que"] : l.pop(i)
            break

print("".join(ans))