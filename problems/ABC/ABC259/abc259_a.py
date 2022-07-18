N, M, X, T, D = map(int, input().split())
a = T - X * D
print(min(T,a+D*M))

