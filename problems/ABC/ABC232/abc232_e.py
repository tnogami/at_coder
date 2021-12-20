H, W, K = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())

a = 0
b = 1
c = 1
d = 0
for i in range(K-1):
    a_next = (W-1)*b + (H-1)*c
    b_next = a + (H-1)*d + (W-2)*b
    c_next = a + (W-1)*d + (H-2)*c
    d_next = c + b + (W+H-4)*d

    a = a_next%998244353
    b = b_next%998244353
    c = c_next%998244353
    d = d_next%998244353

if x1 == x2 and y1 == y2:
    print(a)
elif x1 == x2:
    print(b)
elif y1 == y2:
    print(c)
else:
    print(d)
