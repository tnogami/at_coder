
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
    return set(a)

N, M = map(int, input().split())
A = list(map(int,input().split()))
A.sort()
ans = [True for i in range(10**5+2)]

for a in A:
    p = prime_factorize(a)
    for i in p:
        if ans[i-1] == False: continue
        for j in range(1, 10**9):
            if M < i*j: break
            ans[i*j-1] = False

ans = ans[:M]
print(ans.count(True))
for i,b in enumerate(ans):
    if b == True : print(i+1)
