N, Q = map(int, input().split())
S = input()

top = 0

for i in range(Q):
    q, x = map(int, input().split())
    
    if q == 1:
        top += N - x
    else:
        print(S[(top+x-1)%N])
