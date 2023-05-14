from collections import defaultdict

N = int(input())
A = list(map(int,input().split()))

all_ct = 0
for i in range(1, N+1):
    all_ct += (N - i + 1)*(i//2)

pos = defaultdict(list)

for i, n in enumerate(A):
    pos[n].append(i)

good_ct = 0

for i, l in pos.items():
    if len(l) == 1: continue

    l.sort()
    left_idx = 0
    right_idx = len(l) - 1
    while left_idx != right_idx:
        if l[left_idx] + 1 < N - l[right_idx]:
            good_ct += (l[left_idx] + 1) * (right_idx-left_idx)
            left_idx += 1
        else:
            good_ct += (N - l[right_idx]) * (right_idx-left_idx)
            right_idx -= 1

print(all_ct-good_ct)
