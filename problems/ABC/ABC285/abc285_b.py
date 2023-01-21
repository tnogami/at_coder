N = int(input())
S = input()

for i in range(1,N):
    for k in range(N):
        if N <= k+i: break
        if S[k] == S[k+i]:break
    print(k)
        

