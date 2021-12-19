
S = input()
K = int(input())
N = len(S)

S_list = []
for s in S:
    if s == ".":
        S_list.append(1)
    else:
        S_list.append(0)
S = S_list

right = 0
amount = 0
ans = 0
for left in range(N):
    while right < N and amount + S[right] <= K :#和がKになるまで、rightを右にずらしていく
        amount += S[right]
        right += 1
    
    #rightが行き詰まったので、最大値を更新
    ans = max(ans, right - left)
 
    if right == left:#left loopがrightにまで来たらrightを右に一つずらす　
        right += 1
    else: #次のループでleftが一つ進むので、最後尾の数で割っておく
        amount -= S[left]

print(ans)