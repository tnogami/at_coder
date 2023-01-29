from collections import deque
S = input()
T = input()
lenS = len(S)
lenT = len(T)
not_match_idx = deque()
for i in range(lenT):
    t = T[i]
    s = S[i+lenS-lenT]
    if s != t and s != '?' and t != '?':
        not_match_idx.append(i)

if 0 < len(not_match_idx):
    print("No")
else:
    print("Yes")

end_fault = []
for i in range(lenT):
    if not_match_idx:
        next_not_match_idx = not_match_idx.popleft()
        if next_not_match_idx != i:
            not_match_idx.appendleft(next_not_match_idx)
    
    next_s = S[i]
    if T[i] != next_s and next_s != '?' and T[i] != '?':
        end_fault.append(i)

    if len(not_match_idx) == 0 and len(end_fault) == 0:
        print("Yes")
    else:
        print("No")


