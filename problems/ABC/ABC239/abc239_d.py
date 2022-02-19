A,B,C,D = map(int, input().split())

limit = 210
primes = set()
for i in range(2, limit):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        primes.add(i)

for taka in range(A,B+1):
    out = set()
    for aoki in range(C, D+1):
        num = taka + aoki
        out.add(num)
    if not out&primes:
        print("Takahashi")
        break
else:
    print("Aoki")
