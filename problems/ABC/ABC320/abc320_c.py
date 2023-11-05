from itertools import permutations

N = int(input())
numbers = [list(input()) for _ in range(3)]
s_numbers = list(map(lambda x: set(x), numbers))

if len(s_numbers[0] & s_numbers[1] & s_numbers[2]) == 0:
    print(-1)
else:
    ans = N * 10
    for n in s_numbers[0] & s_numbers[1] & s_numbers[2]:
        for comb in permutations(range(3), 3):
            cur = 0
            for c in comb:
                for t in range(cur, 3 * N + 5):
                    if numbers[c][t % N] == n:
                        cur = t + 1
                        break
            ans = min(ans, cur)

    print(ans)
