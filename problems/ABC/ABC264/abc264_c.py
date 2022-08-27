H1, W1 = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H1)]

H2, W2 = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H2)]

def check(bin1, bin2):
    b_h = -1
    for h in range(H1):
        if ((bin1 >> h) & 1) == 0: continue
        b_h += 1 
        if H2 <= b_h: return False
        b_w = -1
        for w in range(W1):
            if ((bin2 >> w) & 1) == 0: continue 
            b_w += 1
            if W2 <= b_w : return False
            if B[b_h][b_w] != A[h][w] : return False
    
    if b_h == H2-1 and b_w == W2-1:
        return True
    else:
        return False
    
ans = False
for n1 in range(1, 2**H1):
    for n2 in range(1, 2**W1):
        ans = ans or check(n1, n2)

if ans:
    print("Yes")
else:
    print("No")