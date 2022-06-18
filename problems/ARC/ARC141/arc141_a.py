T = int(input())
for _ in range(T):
    N = input()
    length = len(N)
    ans = 0
    for i in range(1,length//2+1):
        if length%i != 0: continue
        first = N[:i]
        if int(first*(length//i)) <= int(N):
            ans = max(ans, int(first*(length//i)))
        else:
            ans = max(ans, int(str(int(first)-1)*(length//i)))
    print(ans)
