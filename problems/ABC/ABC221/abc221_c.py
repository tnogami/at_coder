N = input()

digit = len(N)
ans = 0

for i in range(2**digit): #01の組み合わせ
    a = []
    b = []
    for j in range(digit):  # シフト回数ループ
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う1
            a.append(N[j])
        else:
            b.append(N[j])
        
    if not a or not b:continue

    a.sort(reverse=True)
    b.sort(reverse=True)

    num_a = int("".join(a))
    num_b = int("".join(b))

    ans = max(ans, num_a*num_b)

print(ans)    

