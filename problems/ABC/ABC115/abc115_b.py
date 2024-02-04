N = int(input())
prices = [int(input()) for _ in range(N)]
discount = max(prices)//2
print(sum(prices)-discount)
