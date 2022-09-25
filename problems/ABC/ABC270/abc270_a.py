A, B = map(int, input().split())

def check(a):
    if a == 0:
        return set([])
    elif a ==1:
        return(set([1]))
    elif a ==2:
        return set([2])
    elif a ==3:
        return set([1,2])
    elif a ==4:
        return set([4])
    elif a ==5:
        return set([1,4])
    elif a ==6:
        return set([2,4])
    elif a ==7:
        return set([1,2,4])

aa = check(A)
bb = check(B)

print(sum(aa|bb))