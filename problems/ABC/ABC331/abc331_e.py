N, M, L = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_with_idx = [(a, i) for i, a in enumerate(A)]
B_with_idx = [(b, i) for i, b in enumerate(B)]

A_with_idx.sort()
B_with_idx.sort(reverse=True)

ng_comb = set()

for _ in range(L):
    c, d = map(int, input().split())
    ng_comb.add((c-1, d-1))

ans  = 0

for a in A_with_idx:
    for b in B_with_idx:
        a_price, a_idx = a
        b_price, b_idx = b

        if (a_idx, b_idx) in ng_comb:
            continue

        ans = max(ans, a_price + b_price)
        break


print(ans)