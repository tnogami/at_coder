N = int(input())

is_prime = [True] * 55557
is_prime[0] = False
is_prime[1] = False

for i in range(2, 55555+1):
    k = 2 * i
    while k <= 55555:
        is_prime[k] = False
        k += i

primes = []
for i, b in enumerate(is_prime):
    if b: primes.append(i)

ct = 0
ans = []
for p in primes:
    if p%5 == 1:
        ct += 1
        ans.append(p)
    if ct == N: break
print(*ans)



