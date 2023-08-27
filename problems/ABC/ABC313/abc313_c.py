N = int(input())
A = list(map(int, input().split()))
average = sum(A)//N
amari = sum(A) % average
A.sort(reverse=True)

ans = 0

for a in A:
    if amari == 0:
        if a > average:
            ans += a - average
    else:
        if a > average:
            ans += a - average - 1
            amari -= 1

print(ans)
