def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

N = int(input())
A = list(map(int,input().split()))

twos = []
threes = []

other = set(prime_factorize(A[0]))
if 2 in other:
    other.remove(2)
if 3 in other:
    other.remove(3)

flag = True
for a in A:
    primes = prime_factorize(a)
    two = 0
    three = 0
    for p in primes:
        if p == 2:
            two += 1
        elif p == 3:
            three += 1
        else:
            if p not in other:
                flag = False
    twos.append(two)
    threes.append(three)

if not flag:
    print(-1)
else:
    ans = 0
    min_two = min(twos)
    min_three = min(threes)
    ans += sum(list(map(lambda x:x-min_two, twos)))
    ans += sum(list(map(lambda x:x-min_three, threes)))
    print(ans)




