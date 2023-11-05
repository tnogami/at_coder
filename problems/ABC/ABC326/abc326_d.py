from itertools import permutations
from collections import Counter

N = int(input())
R = input()
C = input()

comb = ['A', 'B', 'C'] + ['.']*(N-3)

field = [['.']*N for _ in range(N)]


def check():
    c_is_ok = True
    for i in range(N):
        tmp = [field[n][i] for n in range(N)]
        ct = Counter(tmp)
        if ct['A'] != 1 or ct['B'] != 1 or ct['C'] != 1:
            c_is_ok = False

        for j in range(3):
            if field[j][i] == '.':
                continue
            if field[j][i] != C[i]:
                c_is_ok = False
            break

        if not c_is_ok:
            return False

    return True


def dfs(n):
    if n == N:
        ret = check()
        if ret:
            print("Yes")
            for f in field:
                print(''.join(f))
            exit()
        return

    for p in permutations(comb, N):
        for i in range(3):
            if p[i] == '.':
                continue
            if p[i] == R[n]:
                r_is_ok = True
            else:
                r_is_ok = False
            break

        if not r_is_ok:
            continue

        field[n] = list(p)
        if n > 0:
            # 各列の数を数える
            is_ok = True
            for i in range(N):
                a_ct = 0
                b_ct = 0
                c_ct = 0

                for j in range(n+1):
                    if field[j][i] == 'A':
                        a_ct += 1
                    elif field[j][i] == 'B':
                        b_ct += 1
                    elif field[j][i] == 'C':
                        c_ct += 1

                if a_ct > 1 or b_ct > 1 or c_ct > 1:
                    is_ok = False
                    break
            if not is_ok:
                field[n] = ['.']*N
                continue
        dfs(n+1)
        field[n] = ['.']*N


dfs(0)

print("No")
