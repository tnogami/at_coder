H, W = map(int, input().split())
if H==1 or W==1:
  print(H*W)
else:
  print((-(-H//2))*(-(-W//2)))