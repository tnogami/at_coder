import bisect

N, K, P = map(int, input().split())
A = list(map(int,input().split()))
A1 = [a for i, a in enumerate(A) if i%2 == 0]
A2 = [a for i, a in enumerate(A) if i%2 == 1]

A1_selected = [[] for i in range(len(A1)+1)]
for i in range(2**len(A1)): #01の組み合わせ
    selected_num = 0
    sum_price = 0
    for j in range(len(A1)):  # シフト回数ループ
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う1
            selected_num += 1
            sum_price += A1[j]
    A1_selected[selected_num].append(sum_price)

A2_selected = [[] for i in range(len(A2)+1)]
for i in range(2**len(A2)): #01の組み合わせ
    selected_num = 0
    sum_price = 0
    for j in range(len(A2)):  # シフト回数ループ
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う1
            selected_num += 1
            sum_price += A2[j]
    A2_selected[selected_num].append(sum_price)

tmp =[]
for a in A1_selected:
    a.sort()
    tmp.append(a)
A1_selected = tmp

tmp =[]
for a in A2_selected:
    a.sort()
    tmp.append(a)
A2_selected = tmp

ans = 0
for i, a_list in enumerate(A1_selected):
    if K < i :break
    n = K-i
    if len(A2_selected) <= n : continue
    for a in a_list:
        p = P-a
        idx = bisect.bisect(A2_selected[n], p)
        ans += idx
print(ans)
