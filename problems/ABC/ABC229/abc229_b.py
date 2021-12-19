A, B = map(int, input().split())
a = str(A)[::-1]
b = str(B)[::-1]

for i in range(min(len(a), len(b))):
    if 10 <= int(a[i])+int(b[i]):
        print("Hard")
        break
else:
    print("Easy")
