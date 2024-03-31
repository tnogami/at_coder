N, A, B = map(int, input().split())
D = [(d-1) % (A+B) for d in list(map(int,input().split()))]
if max(D) - min(D) < A:
    print('Yes')
else:
    print('No')