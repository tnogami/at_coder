Y = int(input())
X = Y%4

if X == 0:
    print(Y+2)
elif X == 1:
    print(Y+1)
elif X == 2:
    print(Y)
else:
    print(Y+3)