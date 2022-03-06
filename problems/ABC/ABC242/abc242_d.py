
S = input()
Q = int(input())
for _ in range(Q):
    t, k = map(int, input().split())
    k -= 1

    #このアルファベットから生成
    C = S[k//pow(2, min(t, 60))]
    n = "ABC".index(C)

    #t回2で割る際に何回あまりを切り捨てたか
    ct = 0
    loop = 0
    for b in bin(k)[2:][::-1]:
        if loop == t:break
        ct += int(b)
        loop += 1
    
    ans = n + t + ct
    print("ABC"[ans%3])
    






    


