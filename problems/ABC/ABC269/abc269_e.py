N = int(input())

a = 1
b = N
c = 1
d = N

while True:
    m = -((-a-b)//2)
    print(f"? {m} {b} {1} {N}")
    T = int(input())
    if T == b-m+1:
        b = m-1
    else:
        a = m

    if a == b:
        break

while True:
    m = -((-c-d)//2)
    print(f"? {1} {N} {m} {d}")
    T = int(input())
    if T == d-m+1:
        d = m-1
    else:
        c = m

    if c == d:
        break

print(f"! {a} {c}")