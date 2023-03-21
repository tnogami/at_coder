N = int(input())
A = [tuple(map(int, input().split())) for _ in range(N)]
for a in A:
    print(sum(a))    

