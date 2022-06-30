N = int(input())
C = list(map(int,input().split()))

cheapest_cost = 10**12
for i, c in enumerate(C):
    if c <= cheapest_cost:
        cheapest_idx = i + 1
        cheapest_cost = c

digits = N // cheapest_cost

ans = [cheapest_idx] * digits
rest = N % cheapest_cost

for i in range(len(ans)):
    if rest == 0:
        break

    for k in range(8,-1,-1):
        if C[k] - cheapest_cost <= rest :
            ans[i] = k + 1
            rest -= C[k] - cheapest_cost
            break
    else:
        break
    
print("".join(list(map(str,ans))))