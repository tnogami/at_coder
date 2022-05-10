N, A, B = map(int, input().split())



for n in range(N*A):

    if (n//A)%2 == 0:
        tairu = ["."*B, "#"*B]
    else:
        tairu = ["#"*B, "."*B]

    ans = []
    for a in range(N):
        ans.append(tairu[a%2])
    print("".join(ans))




