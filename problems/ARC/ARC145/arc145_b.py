N, A, B = map(int, input().split())

def solve(n,a,b):
    if n < a:
        return 0
    
    if a <= b:
        return n - (a-1)

    rep = (n-a) // a
    ret = b * rep + min((n-a)%a+1, b)
    return ret

print(solve(N,A,B))


