S = 'wbwbwwbwbwbw' * 20
W, B = map(int, input().split())

flag = False
for i in range(len(S)-1):
    for j in range(i+1, len(S)):
        s = S[i:j]
        if s.count('w') == W and s.count('b') == B:
            flag = True

if flag:
    print('Yes')
else:
    print('No')