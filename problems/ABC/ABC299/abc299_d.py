N = int(input())
left = 0
right = N-1
while 1 < abs(left-right):
    mid = (left+right)//2
    print(f'? {mid}')
    s = int(input())

    if s == 1:
        right = mid
    else:
        left = mid

print(f'! {left}')

