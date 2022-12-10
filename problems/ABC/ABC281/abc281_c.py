N, T = map(int, input().split())
A = list(map(int,input().split()))
zenbu = sum(A)
T %= zenbu

for i,a in enumerate(A):
    T -= a
    if T < 0:
        idx = i+1
        t = a+T
        break

print(idx, t)