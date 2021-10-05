a, b, c = map(int, input().split())

for i in range(10000):
    if a<=i*c and i*c<=b:
        print(i*c)
        break
else:
    print(-1)