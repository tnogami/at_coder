def div_check(length):
    global L
    global K
    tmp = 0
    end = 0
    count = 0
    for i in range(N):
        tmp = A[i] - end
        if length <= tmp:
            end = A[i]
            count += 1
        if count == K: break
    if count == K and length <= L-end:
        return True
    else:
        return False
    
N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

right = L+1
left = 0

while 1 < right - left :
    if div_check((left+right)//2):
        left = (left+right)//2
    else:
        right = (left+right)//2
print(left)
