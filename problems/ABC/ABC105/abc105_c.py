def mbin_positive_max(l:int)->int:
    ret = 0
    for i in range(l):
        if i%2==0:
            ret += 2**i
    return ret

def mbin_negative_max(l:int)->int:
    ret = 0
    for i in range(l):
        if i%2==1:
            ret += 2**i
    return -ret


N = int(input())

for digit in range(1000):
    if mbin_negative_max(digit) <= N <= mbin_positive_max(digit):
        break

if digit == 0:
    print(0)
else:
    N -= (-2)**(digit-1)
    ans = [0]*digit
    ans[-1] = 1

    while N:
        for n in range(digit):
            if mbin_negative_max(n) <= N <= mbin_positive_max(n):
                ans[n-1] = 1
                N -= (-2)**(n-1)
                break      

    ans = ans[::-1]
            
    print("".join(list(map(str, ans))))
        