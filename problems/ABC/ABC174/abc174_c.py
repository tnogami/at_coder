K = int(input())
if K%2 == 0:
    print(-1)
else:
    a = 7%K
    ans = [1]
    for i in range(K+1):
        ans.append(a)
        a = 10*a + 7
        a %= K
    for i, a in enumerate(ans):
        if a == 0:
            print(i)
            break
    else:
        print(-1)