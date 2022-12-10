N, X = map(int, input().split())
A = list(map(int,input().split()))
for i, a in enumerate(A):
    if a == X:
        print(i+1)