B = int(input())

for i in range(1, 100):
    if B % i == 0 and B//(i**i) == 1:
        print(i)
        break
else:
    print(-1)
