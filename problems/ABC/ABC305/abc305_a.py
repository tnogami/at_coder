N = int(input())

m = N%5

if 3 <= m:
    print(N+(5-m))
else:
    print(N-m)