def to10(n2,n3,n4):
    n6 = n3//2
    ret = 0
    if n4 < n6:
        ret += n4
        n6 -= n4
        if n2 < n6*2:
            ret += n2//2
            return ret
        else:
            ret += n6
            n2 -= 2*n6
            ret += n2//5
            return ret
    else:
        ret += n6
        n4 -= n6

        n8 = n4//2
        n4 = n4%2

        if n2 < n8:
            ret += n2
            return ret
        else:
            ret += n8
            n2 -= n8
            ret += (2*n2+4*n4)//10
            return ret


T = int(input())
for i in range(T):
    n2, n3, n4 = map(int, input().split())
    print(to10(n2,n3,n4))


